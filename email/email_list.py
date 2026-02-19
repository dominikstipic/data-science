import mailbox
from email.header import decode_header
import os
from pathlib import Path

class Email:
    def __init__(self, sender, subject, date, body):
        self.sender = sender
        self.subject = subject
        self.date = date
        self.body = body
    
    def __repr__(self):
        return f"sender={self.sender}, subject={self.subject}, date={self.date}, body={self.body}"

def get_thunderbird_profile():
    """Find Thunderbird profile folder (Windows/Linux/macOS)"""
    if os.name == 'nt':  # Windows
        profile_path = Path.home() / "AppData" / "Roaming" / "Thunderbird" / "Profiles"
    elif os.name == 'posix':
        if os.uname().sysname == 'Darwin':  # macOS
            profile_path = Path.home() / "Library" / "Thunderbird" / "Profiles"
        else:  # Linux
            profile_path = Path.home() / ".thunderbird"
    
    profiles = list(profile_path.glob("*default*")) or list(profile_path.glob("*"))
    return profiles[0] if profiles else None

def safe_decode_header(header):
    """Safely decode email headers with multiple encodings"""
    if not header:
        return ""
    
    decoded_parts = []
    for part, encoding in decode_header(header):
        try:
            if isinstance(part, bytes):
                if encoding:
                    part = part.decode(encoding)
                else:
                    part = part.decode('utf-8', errors='replace')
            decoded_parts.append(part)
        except UnicodeDecodeError:
            decoded_parts.append(str(part, 'latin-1', errors='replace'))
    
    return ''.join(decoded_parts)

def read_thunderbird_inbox(inbox_path=None):
    """Read all emails from Thunderbird Inbox"""
    if not inbox_path:
        profile = get_thunderbird_profile()
        if not profile:
            print("No Thunderbird profile found")
            return
        
        # Try common inbox locations
        inbox_candidates = [
            profile / "Mail" / "Local Folders" / "Inbox",
            profile / "ImapMail" / "*" / "Inbox",
            next((profile / "Mail").glob("*/Inbox"), None)
        ]
        
        inbox_path = next((p for p in inbox_candidates if p.exists()), None)
    
    if not inbox_path or not inbox_path.exists():
        print(f"Inbox not found at {inbox_path}")
        return
    
    # Use mailbox.Mboxrd (Thunderbird format)
    mbox = mailbox.mbox(str(inbox_path), create=False)
    
    count = 0
    for i, message in enumerate(mbox):
        count += 1
        sender = safe_decode_header(message.get('From', 'Unknown'))
        subject = safe_decode_header(message.get('Subject', 'No Subject'))
        date = safe_decode_header(message.get('Date', 'No Date'))
        body = ""
        if message.is_multipart():
            for part in message.walk():
                if part.get_content_type() == "text/plain":
                    try:
                        body = part.get_payload(decode=True).decode('utf-8', errors='replace')
                        break
                    except:
                        body = part.get_payload(decode=True).decode('latin-1', errors='replace')
                        break
        else:
            try:
                body = message.get_payload(decode=True).decode('utf-8', errors='replace')
            except:
                body = message.get_payload(decode=True).decode('latin-1', errors='replace')
            e = Email(sender, subject, date, body)
            yield e
    mbox.close()

def read_with_fallback_encoding(file_path):
    """Read file with multiple encoding attempts"""
    encodings_to_try = ['utf-8', 'latin-1', 'cp1252', 'iso-8859-1']
    
    for encoding in encodings_to_try:
        try:
            with open(file_path, 'r', encoding=encoding, errors='replace') as f:
                return f.read()
        except UnicodeDecodeError:
            continue
    return None

def extract_email(line):
    result = ""
    flag = False
    for s in line:
        if s == ">":
            return result
        elif s == "<":
            flag = True
        elif flag == True:
            result += s
    return result

def process_from_file():
    emails = set()
    files = os.listdir("Emails")
    for f in files:
        with open(f"Emails/{f}", "r") as fp:
            try:
                for line in fp:
                    if line.startswith("From:"):
                        _,b = line.split(":")
                        b = b.strip()
                        e = extract_email(b)
                        if "@" in e:
                            emails = emails.union([e])
            except Exception:
                print(f"EXC {line}")

    with open("emails.txt", "w") as fp:
        for e in emails:
            fp.write(e + "\n")

def process():
    gen = read_thunderbird_inbox()
    result = []
    for e in gen:
        e = extract_email(e.sender)
        if "@" in e:
            result.append(e)
    return set(result)

if __name__ == "__main__":
    gen = process()
    for g in gen:
        print(g)

    