# Project Venom: Cloud-Native Deception & Intelligence Grid

## 🚀 Overview
Project Venom is a high-integrity honeypot system deployed on AWS to monitor real-time threat landscapes. It utilizes containerization for environment isolation and a custom Python engine to capture, parse, and geolocate unauthorized access attempts, delivering instant intelligence via the Telegram Bot API.

## 🛠️ Technical Stack
* **Infrastructure**: AWS EC2 with strict Security Group ingress policies.
* **Virtualization**: Docker (OpenCanary) for decoy environment isolation.
* **Language**: Python 3 for real-time log parsing and Geolocation API integration.
* **Automation**: Linux `systemd` for self-healing service management and persistence.
* **Alerting**: Telegram Bot API for asynchronous push notifications.

## 🔒 Security & Integrity Features
* **Host Hardening**: Administrative SSH (Port 22) is restricted to a specific management IP, isolating the host from the public internet.
* **Namespace Isolation**: All decoy services run within Docker containers to prevent attackers from interacting with the host OS.
* **Resilience**: The system features an automatic "always-on" restart policy for both the container and the monitoring script.
* **Health Monitoring**: Implemented a 24-hour heartbeat notification to ensure system operational status.

## 📂 Project Structure
* `stinger.py`: The Python monitoring engine (Sanitized for public release).
* `opencanary.conf`: Configuration file defining HTTP, FTP, and SSH-trap behavior.
* `venom-stinger.service`: Systemd unit file for background process management.
* `deploy-bait.sh`: Shell script for standardized Docker deployment.

## 📊 Operational Flow
1. **The Bait**: OpenCanary (inside Docker) mimics high-value services like a Synology NAS.
2. **The Capture**: Unauthorized interactions are logged as structured JSON.
3. **The Analysis**: The Python 'Stinger' parses logs and queries Geolocation APIs for attribution.
4. **The Strike**: Formatted alerts are pushed to the administrator's mobile device.

## 🔄 Evolution: Overcoming Venom 1.0
The initial prototype (v1.0) suffered from operational fragility. Administrative ports were exposed to the public internet, and processes required manual intervention.

**Venom 2.0 improvements:**
- **Hardened Ingress:** Successfully migrated to a "Least Privilege" network model by restricting administrative access to a single source IP.
- **Autonomous Operations:** Transitioned from manual execution to a fully managed systemd architecture, achieving 100% process persistence.
- **Containerized Isolation:** Moved decoy services into Docker to decouple the threat environment from the host operating system.

---

*Note: This repository is for educational and portfolio purposes. Actual credentials and private keys have been removed to maintain secret management integrity.*
