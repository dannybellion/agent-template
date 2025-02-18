# Avalon Email Content Blocks

A collection of HTML email snippets to use for transactional customer comms.

---

## How to Use This Template

This collection of HTML snippets is designed to help you efficiently compose branded, modular, and responsive transactional emails. Below are key pointers to get you started:

1. **Email Wrapper**: Always begin by using the **Email Wrapper**. This wrapper provides a consistent layout, branding, and ensures responsiveness across all devices. It includes a branded header and footer, including key links and legal info.
    - All email content should be placed within the **Main Content Wrapper** provided inside the Email Wrapper. Look for the comment `<!-- Insert Modular Blocks Here -->`
    - Update the preview text, labelled with `<!-- Preview Text -->`
    - Update the **Header Image** source, or remove if not needed, labelled `<!-- Header Image -->`
2. **Main Content Blocks**: The template is made up of reusable content blocks such as **Large Intro**, **Heading and Paragraph**, **Feature Highlights List**, and more. These blocks are designed to simplify the composition process and maintain a uniform appearance across all communications.
3. **Divider Line**: To keep the email visually organised, use the **Divider Line** to separate different sections of the content. This helps make the email easier to read by creating digestible and visually distinct areas.
4. **Calls to Action**: Use the **Centred Button** or **Inline Link** to provide clear prompts for recipients to take action. Make sure to update both the `if` query and `<a>` tag link to reflect the desired URLs and button labels.
5. **Bullet Lists and Feature Highlights**: For presenting key points or benefits, use the **Bullet List** or **Feature Highlights** to ensure content is concise and scannable. This is particularly useful for marketing or informational emails to quickly convey key information.
6. **Signature Text**: Conclude each email with the **Signature Text** block.

---

## Template

### Email Wrapper

**Purpose:** Provides a structured and consistent outer framework for the email's content, ensuring a unified layout, branding, and responsive design that enhances readability and visual appeal across devices.

<aside>
⚠️

Please update the preview text and either update the *Header Image* source or remove the image area entirely if none is needed.

</aside>

<aside>
ℹ️

AWAITING FINAL IMAGE URLS

</aside>

```html
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html lang="en" xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office">
<head>
	<!--[if gte mso 9]>
	<xml>
		<o:OfficeDocumentSettings>
		<o:AllowPNG/>
		<o:PixelsPerInch>96</o:PixelsPerInch>
		</o:OfficeDocumentSettings>
	</xml>
	<![endif]-->
	<meta http-equiv="Content-type" content="text/html; charset=utf-8" />
	<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1" />
	<meta http-equiv="X-UA-Compatible" content="IE=edge" />
	<meta name="format-detection" content="date=no" />
	<meta name="format-detection" content="address=no" />
	<meta name="format-detection" content="telephone=no" />
	<meta name="x-apple-disable-message-reformatting" />
	<link rel="icon" href="https://production-cmscdn.capitalontap.com/media/media/3u1b4jr4/favicon.svg" />
	<link rel="apple-touch-icon" href="https://production-cmscdn.capitalontap.com/media/media/3u1b4jr4/favicon.svg" />
	<title>Email Template</title>
	<!--[if !mso]><!-->	
	<style type="text/css" media="all"> 
		@import url('https://fonts.googleapis.com/css2?family=Epilogue:ital,wght@0,100..900;1,100..900&family=Inter:ital,opsz,wght@0,14..32,100..900;1,14..32,100..900&display=swap');
	</style>
	<!--<![endif]-->
	<!--[if gte mso 9]>
	<style type="text/css" media="all">
		sup { font-size: 100% !important; }
	</style>
	<![endif]-->

	<style type="text/css" media="screen">
		body { padding:0 !important; margin:0 auto !important; display:block !important; min-width:100% !important; width:100% !important; background:#E6E6E8; -webkit-text-size-adjust:none }
		a { color:#000814; text-decoration:none }
		p { margin:0 !important; Margin:0 !important } 

		table { mso-table-lspace:0pt; mso-table-rspace:0pt; }
		img { margin: 0 !important; -ms-interpolation-mode: bicubic; }
		img, a img { border:0; outline:none; text-decoration:none; }
		#outlook a { padding:0; }
		.ReadMsgBody, .ExternalClass { width:100%; }
		div,p,a,li,td,blockquote { mso-line-height-rule:exactly; }
		a[href^=tel],a[href^=sms] { color:inherit; text-decoration:none; }
		a[x-apple-data-detectors] { color:inherit !important; text-decoration:none !important; font-size:inherit !important; font-family:inherit !important; font-weight:inherit !important; line-height:inherit !important; }
		.x-gmail-data-detectors, .x-gmail-data-detectors *, .aBn { border-bottom: 0 !important; cursor: default !important; }
		.a6S { display: none !important; opacity: 0.01 !important; }
		u + #body a { color: inherit !important; font-size: inherit !important; font-family: inherit !important; font-weight: inherit !important; line-height: inherit !important; }

		.l-blue a { color: #2B4DC7; }
		.l-grey a { color: #4D525B; }
		.l-white a { color: #ffffff; }
		.l-black a { color: #000000; }

		/* Mobile styles */
		@media only screen and (max-width: 480px) {
			.mpx-16 { padding-left: 16px !important; padding-right: 16px !important; }
			.m-shell { width: 100% !important; min-width: 100% !important; }
			.fluid-img img { width: 100% !important; max-width: 100% !important; height: auto !important; max-height: none !important; }
			.m-hide { display: none !important; width: 0 !important; height: 0 !important; font-size: 0 !important; line-height: 0 !important; }
		}
	</style>
</head>

  <body style="padding: 0 !important; margin: 0 auto !important; display: block !important; min-width: 100% !important; width: 100% !important; background: #e6e6e8; -webkit-text-size-adjust: none">
    <div align="center">
      <table class="mbg-transp" width="100%" border="0" cellspacing="0" cellpadding="0" style="margin: 0; padding: 0; width: 100%; height: auto" bgcolor="#E6E6E8">
        <!-- Preview Text -->
        <tr class="m-hide" style="mso-hide: all">
          <td style="font-size: 0pt; line-height: 0pt">Preview text goes here for email clients</td>
        </tr>

        <!-- Main Wrapper -->
        <tr>
          <td align="center">
            <table width="700" border="0" cellspacing="0" cellpadding="0" class="m-shell">
              <tr>
                <td style="font-size: 0pt; line-height: 0pt; padding: 0; margin: 0">
                  <!-- Header Block -->
                  <tr>
                    <td style="font-size: 0pt; line-height: 0pt" bgcolor="#000814">
                      <table width="100%" border="0" cellspacing="0" cellpadding="0">
                        <tr>
                          <td style="text-align: center; padding-top: 24px; padding-bottom: 24px">
                            <a href="#" target="_blank">
                              <img src="https://userimg-assets.customeriomail.com/images/client-env-99709/1727186661455_logo_01J8J5HW7JPSQ2S3A87N850NXQ.png" width="162" height="24" border="0" alt="Company Logo" />
                            </a>
                          </td>
                        </tr>
                      </table>

                      <!-- Header Image -->
                      <div class="fluid-img" style="font-size: 0pt; line-height: 0pt; text-align: left">
                        <img src="https://userimg-assets.customeriomail.com/images/client-env-99709/1727186640069_backbook-hero_01J8J5H7BFECSSBQ0X11P0QJ2G.jpg" width="700" height="406" border="0" alt="Hero Image" />
                      </div>
                      <!-- END Header Image -->
                    </td>
                  </tr>
                  <!-- END Header Block -->

                  <!-- General Content Wrapper -->
                  <tr>
                    <td class="mpx-16" style="font-size: 0pt; line-height: 0pt; padding-top: 40px; padding-bottom: 40px; padding-left: 56px; padding-right: 56px" bgcolor="#ffffff">
                      <table width="100%" border="0" cellspacing="0" cellpadding="0">
                        <!-- Insert Modular Blocks Here -->

                      </table>
                    </td>
                  </tr>
                  <!-- END General Content Wrapper -->
                </td>
              </tr>
            </table>

            <table width="700" border="0" cellspacing="0" cellpadding="0" class="m-shell">
                <!-- Footer Block -->
                <tr>
                    <td class="pt-24 px-16" bgcolor="#000001" style="padding-top: 24px; padding-left: 16px; padding-right: 16px">
                      <table width="100%" border="0" cellspacing="0" cellpadding="0">
                        <tr>
                          <td class="text fz-14 lh-24 a-center c-white l-white pb-24" style="font-family: 'Inter', Arial, sans-serif; font-size: 14px; line-height: 24px; text-align: center; color: #fffffe; padding-bottom: 24px">
                            <a href="tel:020 8962 7401" target="_blank" class="link c-white" style="text-decoration: none; color: #fffffe">020 8962 7401</a>
                            &nbsp;
                            <span class="c-grey" style="color: #4d525b">|</span>
                            &nbsp;
                            <a href="mailto:contact@capitalontap.com" target="_blank" class="link c-white" style="text-decoration: none; color: #fffffe">contact@capitalontap.com</a>
                            &nbsp;
                            <span class="c-grey" style="color: #4d525b">|</span>
                            &nbsp;
                            <a href="https://www.capitalontap.com/" target="_blank" class="link c-white" style="text-decoration: none; color: #fffffe">www.capitalontap.com</a>
                          </td>
                        </tr>
                        <tr>
                          <td class="pb-24" align="center" style="padding-bottom: 24px">
                            <!-- Socials -->
                            <table border="0" cellspacing="0" cellpadding="0">
                              <tr>
                                <td class="img px-12" style="font-size: 0pt; line-height: 0pt; text-align: left; padding-left: 12px; padding-right: 12px">
                                  <a href="https://www.facebook.com/CapitalOnTap/" target="_blank">
                                    <img src="https://userimg-assets.customeriomail.com/images/client-env-99709/1701256331939_icons8-facebook-48_01HGDCF0PZ9T396SS399NP2ZTE.png" width="25" height="25" border="0" alt="" />
                                  </a>
                                </td>
                                <td class="img px-12" style="font-size: 0pt; line-height: 0pt; text-align: left; padding-left: 12px; padding-right: 12px">
                                  <a href="https://twitter.com/CapitalOnTap/" target="_blank">
                                    <img src="https://userimg-assets.customeriomail.com/images/client-env-99709/1701256785963_icons8-twitterx-50_01HGDCWW33GD70GDVPS7CGV8TM.png" width="24" height="24" border="0" alt="" />
                                  </a>
                                </td>
                                <td class="img px-12" style="font-size: 0pt; line-height: 0pt; text-align: left; padding-left: 12px; padding-right: 12px">
                                  <a href="https://www.linkedin.com/company/capital-on-tap/" target="_blank">
                                    <img src="https://userimg-assets.customeriomail.com/images/client-env-99709/1701256574016_icons8-linkedin-48_01HGDCPD3Z0M83QE9EGV53KBPC.png" width="24" height="24" border="0" alt="" />
                                  </a>
                                </td>
                                <td class="img px-12" style="font-size: 0pt; line-height: 0pt; text-align: left; padding-left: 12px; padding-right: 12px">
                                  <a href="https://www.instagram.com/capitalontap/" target="_blank">
                                    <img src="https://userimg-assets.customeriomail.com/images/client-env-99709/1701256732470_icons8-instagram-48_01HGDCV83N2J3AJTR5BGH4S596.png" width="24" height="24" border="0" alt="" />
                                  </a>
                                </td>
                                <td class="img px-12" style="font-size: 0pt; line-height: 0pt; text-align: left; padding-left: 12px; padding-right: 12px">
                                  <a href="mailto:contact@capitalontap.com" target="_blank">
                                    <img src="https://userimg-assets.customeriomail.com/images/client-env-99709/1701256876929_icons8-email-48_01HGDCZMXWSJYJDJFHKGDCRDK0.png" width="24" height="24" border="0" alt="" />
                                  </a>
                                </td>
                              </tr>
                            </table>
                            <!-- END Socials -->
                          </td>
                        </tr>
                        <tr>
                          <td class="pb-24" align="center" style="padding-bottom: 24px">
                            <!-- App Buttons -->
                            <table class="mw-100p" border="0" cellspacing="0" cellpadding="0">
                              <tr>
                                <td class="fluid-img px-8" style="font-size: 0pt; line-height: 0pt; text-align: left; padding-left: 8px; padding-right: 8px">
                                  <a href="https://play.google.com/store/apps/details?id=com.cot.app" target="_blank">
                                    <img src="https://userimg-assets.customeriomail.com/images/client-env-99709/1736871395687_Google%20Play%20Button_01JHJSMGCCDQCK3WH5F8GSP00F.png" width="164" height="48" border="0" alt="" />
                                  </a>
                                </td>
                                <td class="fluid-img px-8" style="font-size: 0pt; line-height: 0pt; text-align: left; padding-left: 8px; padding-right: 8px">
                                  <a href="https://apps.apple.com/gb/app/capital-on-tap/id1398201114" target="_blank">
                                    <img src="https://userimg-assets.customeriomail.com/images/client-env-99709/1736871394852_AppStore%20button_01JHJSMFNWMJG0347YZ5P4BH8X.png" width="146" height="48" border="0" alt="" />
                                  </a>
                                </td>
                              </tr>
                            </table>
                            <!-- END App Buttons -->
                          </td>
                        </tr>
                      </table>
                    </td>
                  </tr>
                  <tr>
                    <td class="text fz-12 lh-16 a-center c-grey l-grey py-24 px-56 mpx-16" style="font-weight: 500; font-family: 'Inter', Arial, sans-serif; font-size: 12px; line-height: 16px; text-align: center; color: #4d525b; padding-top: 24px; padding-bottom: 24px; padding-left: 56px; padding-right: 56px" bgcolor="#e6e6e8">New Wave Capital Limited (trading as Capital on Tap) is a private limited company incorporated in England and Wales under registered number 07959823 which has its registered office at 27 Old Gloucester Street, London, England, WC1N 3AX. Capital on Tap is authorised and regulated by the Financial Conduct Authority (firm reference number 625592 in respect of consumer credit activities) and is authorised by the Financial Conduct Authority under the Electronic Money Regulations 2011, firm reference 900922, for the issuing of electronic money.</td>
                  </tr>
                  <!-- END Footer Block -->
            </table>
        
          </td>
        </tr>
      </table>
      <!--- END Main Wrapper-->
    </div>
  </body>
</html>
```

---

## Content Blocks

### Large **Intro**

![Screenshot 2024-12-06 at 12.01.41.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/c3300230-0f49-45f5-a5ac-64f980a38bad/2b6e75b1-a1b5-452d-a6ef-5ce016700cbd/8dc147a5-ecd5-4984-a636-ffc02a4e7e3a.png)

**Purpose**: Provide a warm greeting and introduce the email topic.

- Include a heading and call to action in bold, attention-grabbing introduction for emails focused on readers taking a desired action.
- Or, customise by removing the heading and/or call to action for simple transactional emails where the priority is directing readers directly to the body content.

<aside>
⚠️

There are two button labels and link URLs that must be updated when used. One in the `if` query, and one in the `<a>` tag.

</aside>

```html
<!-- Large Intro -->
<table width="100%" border="0" cellspacing="0" cellpadding="0" style="padding-top: 16px; padding-bottom: 16px;">

<!-- Heading -->
<tr>
	<td class="a-center" style="font-weight: bold; color:#000814; font-family:'Epilogue', Arial, sans-serif; font-size: 24px; line-height: 32px; text-align:center; padding-bottom: 16px;">
		This is a title or heading for the email
	</td>
</tr>
<!-- END Heading -->

<!-- Paragraph -->
<tr>
	<td class="c-grey l-grey a-center" style="font-family:'Inter', Arial, sans-serif; font-size: 16px; line-height: 28px; color:#4D525B; text-align:center; padding-bottom: 16px;">
		This is an intro paragraph to provide a warm greeting and introduce the email topic.
	</td>
</tr>
<!-- END Paragraph -->

<!-- Call to Action -->
<tr>
	<td  style="font-family: 'Inter', Arial, Helvetica, sans-serif; font-size: 16px; line-height: 20px; font-weight: normal; mso-line-height-alt: 0px; mso-ansi-font-size: 0;" align="center">
		
		<!-- Button -->
		<!--[if mso]>
		<v:roundrect xmlns:v="urn:schemas-microsoft-com:vml" xmlns:w="urn:schemas-microsoft-com:office:word" href="https://www.capitalontap.com/" style="width:160px;height:40px;v-text-anchor:middle" arcsize="100%" fillcolor="#fdb728"  stroke="f">
		<v:textbox>
		<w:anchorlock></w:anchorlock>
		<center style="font-family: Arial, Helvetica, sans-serif; font-size: 16px; mso-line-height-alt: 20px; mso-text-raise: 1px; mso-line-height-rule: exactly; font-weight: normal; color: #000814">
		Learn more
		</center>
		</v:textbox>
		</v:roundrect>
		<![endif]-->
		<a href="https://www.capitalontap.com/" style="margin: 0; box-sizing: border-box; text-decoration: inherit; font-size: 16px; font-weight: normal; color: #000814; font-family: 'Inter', Arial, Helvetica, sans-serif; width: 160px; line-height: 20px; border-radius: 100px; background-color: #fdd051; background: linear-gradient(to bottom, #fdd051 0%,#fcae2a 100%); display: inline-block; text-align: center; padding: 10px; mso-hide: all;">
		Learn more
		</a>
		<!-- END Button -->
		
	</td>
</tr>
<!-- END Call to Action -->

</table>
<!-- END Large Intro -->
```

### Heading and Paragraph

![Screenshot 2024-12-06 at 12.02.42.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/c3300230-0f49-45f5-a5ac-64f980a38bad/36133d45-15a9-4a56-bf70-c6d0bbbbdcf4/Screenshot_2024-12-06_at_12.02.42.png)

**Purpose:** To introduce and communicate key information such as further explanatory content within the body of the email.

```html
<!-- Heading and Paragraph -->
<table width="100%" border="0" cellspacing="0" cellpadding="0" style="padding-top: 24px; padding-bottom: 24px;">
    <!-- Heading -->
    <tr>
        <td style="font-weight: bold; font-family: 'Epilogue', Arial, sans-serif; font-size: 24px; line-height: 32px; color: #000814; padding-bottom: 16px;">
            Heading Text
        </td>
    </tr>
    <!-- END Heading -->
    <!-- Paragraph -->
    <tr>
        <td style="font-family: 'Inter', Arial, sans-serif; font-size: 16px; line-height: 28px; color: #4D525B;">
            Paragraph text that provides more information about the topic introduced by the header. This text is designed to wrap over multiple lines and provide sufficient context or details.
        </td>
    </tr>
    <!-- End Paragraph -->
    <!-- Repeat paragraphs as needed -->
</table>
<!-- END Heading and Paragraph -->
```

### Paragraph

![Screenshot 2024-12-06 at 12.02.42.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/c3300230-0f49-45f5-a5ac-64f980a38bad/de0055b3-e817-4cdc-a437-85365bd2b82e/b570f91a-2a6c-472a-bbec-6a9e60850e12.png)

**Purpose:** For further explanatory content within the body of the email.

```html
<!-- Paragraph -->
<table width="100%" border="0" cellspacing="0" cellpadding="0" style="padding-top: 24px; padding-bottom: 24px;">
    <!-- Paragraph -->
    <tr>
        <td style="font-family: 'Inter', Arial, sans-serif; font-size: 16px; line-height: 28px; color: #4D525B;">
            Paragraph text that provides more information about the topic introduced by the header. This text is designed to wrap over multiple lines and provide sufficient context or details.
        </td>
    </tr>
    <!-- End Paragraph -->
    <!-- Repeat paragraphs as needed -->
</table>
<!-- END Paragraph -->
```

### Divider Line

![Screenshot 2024-12-06 at 12.01.50.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/c3300230-0f49-45f5-a5ac-64f980a38bad/6ac929aa-6194-4ddb-a220-43c392db8742/Screenshot_2024-12-06_at_12.01.50.png)

**Purpose**: Visually separate sections of the email with a thin line.

```html
<!-- Divider Line -->
<table width="100%" border="0" cellspacing="0" cellpadding="0" style="padding-top: 16px; padding-bottom: 16px;">
<tr>
    <td style="border-bottom: 1px solid #e6e6e8; font-size: 0pt; line-height: 0pt; padding-top: 1px; padding-bottom: 1px;">
        &nbsp;
    </td>
</tr>
</table>
<!-- END Divider Line -->
```

### Feature Highlights List

![Screenshot 2024-12-06 at 12.02.01.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/c3300230-0f49-45f5-a5ac-64f980a38bad/524c2a40-6b2c-4159-abfb-cb68afe4c5f9/Screenshot_2024-12-06_at_12.02.01.png)

**Purpose**: Highlight key benefits or features in a visually appealing format. Reserved for content with a positive customer context, such as marketing or onboarding.

```html
<!-- Feature Highlights  -->
<table width="100%" border="0" cellspacing="0" cellpadding="0" style="padding-top: 16px; padding-bottom: 16px;">
    <!-- List Item -->
    <tr>
        <td  width="16" valign="top" style="font-size:0pt; line-height:0pt; text-align:left; padding-bottom: 8px;">
            <table width="100%" border="0" cellspacing="0" cellpadding="0">
                <tr>
                    <td  style="font-size:0pt; line-height:0pt; text-align:left; padding-top: 6px;">
                        <img src="https://userimg-assets.customeriomail.com/images/client-env-99709/1727186638487_ico_check_01J8J5H5TF7D21GSE0K43J5WRZ.png" width="16" height="16" border="0" alt="image" />
                    </td>
                </tr>
            </table>
        </td>
        <td  valign="top" style="color:#000814; font-family:'Inter', Arial, sans-serif; text-align:left; font-size: 16px; line-height: 28px; padding-left: 8px; padding-bottom: 8px;">
            <strong><span style="font-weight: 600;">Unlimited lounge access:</span></strong> Relax at over 1,600 airport lounges worldwide with Priority Pass&trade;. Includes two free guest passes each year, with additional guests for just &pound;20.
        </td>
    </tr>
    <!-- END List Item -->
    
    <!-- List Item -->
    <tr>
        <td  width="16" valign="top" style="font-size:0pt; line-height:0pt; text-align:left; padding-bottom: 8px;">
            <table width="100%" border="0" cellspacing="0" cellpadding="0">
                <tr>
                    <td  style="font-size:0pt; line-height:0pt; text-align:left; padding-top: 6px;">
                        <img src="https://userimg-assets.customeriomail.com/images/client-env-99709/1727186638487_ico_check_01J8J5H5TF7D21GSE0K43J5WRZ.png" width="16" height="16" border="0" alt="image" />
                    </td>
                </tr>
            </table>
        </td>
        <td  valign="top" style="color:#000814; font-family:'Inter', Arial, sans-serif; text-align:left; font-size: 16px; line-height: 28px; padding-left: 8px; padding-bottom: 8px;">
            <strong><span style="font-weight: 600;">Redeem points for Avios:</span></strong> Convert your points to Avios easily, so you can fly further.
        </td>
    </tr>
    <!-- END List Item -->
    
</table>
<!-- END Feature Highlights List -->
```

### Bullet List

![Screenshot 2024-12-06 at 12.02.12.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/c3300230-0f49-45f5-a5ac-64f980a38bad/f097a736-d441-4b0c-b3e6-2e23e0c0baee/Screenshot_2024-12-06_at_12.02.12.png)

**Purpose:** Presents key points or features in a concise, easy-to-read format.

```html
<!-- Bullet List -->
<table width="100%" border="0" cellspacing="0" cellpadding="0" style="padding-top: 16px; padding-bottom: 16px;">
    <tr>
        <td  style="padding-left: 8px;">
            <table width="100%" border="0" cellspacing="0" cellpadding="0">
                <tr>
                    <td class="c-grey l-grey" width="10" valign="top" style="font-family:'Inter', Arial, sans-serif; text-align:left; font-size: 16px; line-height: 24px; color:#4D525B;">&bull;</td>
                    <td class="c-grey l-grey" valign="top" style="font-family:'Inter', Arial, sans-serif; text-align:left; font-size: 16px; line-height: 24px; color:#4D525B; padding-left: 6px; padding-bottom: 8px;">
                        Uncapped 1% cashback
                    </td>
                </tr>
                <tr>
                    <td class="c-grey l-grey" width="10" valign="top" style="font-family:'Inter', Arial, sans-serif; text-align:left; font-size: 16px; line-height: 24px; color:#4D525B;">&bull;</td>
                    <td class="c-grey l-grey" valign="top" style="font-family:'Inter', Arial, sans-serif; text-align:left; font-size: 16px; line-height: 24px; color:#4D525B; padding-left: 6px; padding-bottom: 8px;">
                        Up to 42 days interest-free spending
                    </td>
                </tr>
                <tr>
                    <td class="c-grey l-grey" width="10" valign="top" style="font-family:'Inter', Arial, sans-serif; text-align:left; font-size: 16px; line-height: 24px; color:#4D525B;">&bull;</td>
                    <td class="c-grey l-grey" valign="top" style="font-family:'Inter', Arial, sans-serif; text-align:left; font-size: 16px; line-height: 24px; color:#4D525B; padding-left: 6px; padding-bottom: 8px;">
                        Unlimited employee cards
                    </td>
                </tr>
            </table>
        </td>
    </tr>
  </table>
<!-- Bullet List -->
```

### Numbered List

![Screenshot 2024-12-10 at 15.23.33.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/c3300230-0f49-45f5-a5ac-64f980a38bad/e7a81659-46f2-4adb-a868-6bde99b5ca27/Screenshot_2024-12-10_at_15.23.33.png)

**Purpose:** Presents a list of items or steps in a process in an easy-to-read format.

```html
<!-- Numbered List -->
<table width="100%" border="0" cellspacing="0" cellpadding="0" style="padding-top: 16px; padding-bottom: 16px;">
    <tr>
        <td  style="padding-left: 8px;">
            <table width="100%" border="0" cellspacing="0" cellpadding="0">
                <tr>
                    <td class="c-grey l-grey" width="10" valign="top" style="font-family:'Inter', Arial, sans-serif; text-align:left; font-size: 16px; line-height: 24px; color:#000814; font-weight: bold;">1.</td>
                    <td class="c-grey l-grey" valign="top" style="font-family:'Inter', Arial, sans-serif; text-align:left; font-size: 16px; line-height: 24px; color:#4D525B; padding-left: 6px; padding-bottom: 8px;">
                        This is the first item in the numbered list. These can be many sentences that wrap over multiple lines.
                    </td>
                </tr>
                <tr>
                    <td class="c-grey l-grey" width="10" valign="top" style="font-family:'Inter', Arial, sans-serif; text-align:left; font-size: 16px; line-height: 24px; color:#000814; font-weight: bold;">2.</td>
                    <td class="c-grey l-grey" valign="top" style="font-family:'Inter', Arial, sans-serif; text-align:left; font-size: 16px; line-height: 24px; color:#4D525B; padding-left: 6px; padding-bottom: 8px;">
                        And another item in the numbered list.
                    </td>
                </tr>
                <tr>
                    <td class="c-grey l-grey" width="10" valign="top" style="font-family:'Inter', Arial, sans-serif; text-align:left; font-size: 16px; line-height: 24px; color:#000814; font-weight: bold;">3.</td>
                    <td class="c-grey l-grey" valign="top" style="font-family:'Inter', Arial, sans-serif; text-align:left; font-size: 16px; line-height: 24px; color:#4D525B; padding-left: 6px; padding-bottom: 8px;">
                        Plus, a third item in the numbered list etc.
                    </td>
                </tr>
            </table>
        </td>
    </tr>
  </table>
<!-- END Numbered List -->
```

### Table

![Screenshot 2024-12-06 at 12.02.33.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/c3300230-0f49-45f5-a5ac-64f980a38bad/cea34eca-4272-48f0-a397-0f96a586d8f0/Screenshot_2024-12-06_at_12.02.33.png)

**Purpose:** Display tabular information with a heading, introductory text, and rows containing labels and corresponding values. Includes *Table Row*, for displaying data in a consistent way, and *Emphasised Table Row*, to bring particular attention to key information such as a sum total.

```html
<!-- Table -->
<table width="100%" border="0" cellspacing="0" cellpadding="0" style="padding-top: 16px; padding-bottom: 16px;">
			
    <!-- Table Row -->
    <tr>
        <td style="width: 50%; font-family: 'Inter', Arial, sans-serif; font-size: 16px; font-weight: bold; line-height: 24px; color: #000814; text-align: left; padding: 16px 0; border-top: 1px solid #E6E6E8;">
            Table row label
        </td>
        <td style="width: 50%; font-family: 'Inter', Arial, sans-serif; font-size: 16px; font-weight: normal; line-height: 24px; color: #4D525B; text-align: right; padding: 16px 0; border-top: 1px solid #E6E6E8;">
            Table row value
        </td>
    </tr>
    <!-- END Table Row -->
    
    <!-- Table Row -->
    <tr>
        <td style="width: 50%; font-family: 'Inter', Arial, sans-serif; font-size: 16px; font-weight: bold; line-height: 24px; color: #000814; text-align: left; padding: 16px 0; border-top: 1px solid #E6E6E8;">
            This table row label wraps over many lines
        </td>
        <td style="width: 50%; font-family: 'Inter', Arial, sans-serif; font-size: 16px; font-weight: normal; line-height: 24px; color: #4D525B; text-align: right; padding: 16px 0; border-top: 1px solid #E6E6E8;">
            Table row value
        </td>
    </tr>
    <!-- END Table Row -->
    
    <!-- Emphasised Table Row -->
    <tr>
        <td style="width: 50%; font-family: 'Inter', Arial, sans-serif; font-size: 16px; font-weight: bold; line-height: 24px; color: #000814; text-align: left; padding: 16px 0; border-top: 1px solid #000814; border-bottom: 1px solid #000814;">
            Table row label
        </td>
        <td style="width: 50%; font-family: 'Inter', Arial, sans-serif; font-size: 16px; font-weight: normal; line-height: 24px; color: #4D525B; text-align: right; padding: 16px 0; border-top: 1px solid #000814; border-bottom: 1px solid #000814;">
            Table row value
        </td>
    </tr>
    <!-- END Table Row -->
    
    <!-- Remove or repeat rows as needed -->
</table>
<!-- END Table -->
```

### Centred Button

![Screenshot 2024-12-06 at 12.02.52.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/c3300230-0f49-45f5-a5ac-64f980a38bad/76578088-ccfb-4094-9f33-db46adce2578/Screenshot_2024-12-06_at_12.02.52.png)

**Purpose:** To provide a clear, visually distinct call-to-action, prompting the recipient to take immediate action such as visiting a website, signing up, or learning more.

<aside>
⚠️

There are two button labels and link URLs, one in the `if` query, and one in the `<a>` tag. Please ensure both are updated when used.

</aside>

```html
<!-- Centred Button -->
<table width="100%" border="0" cellspacing="0" cellpadding="0" style="padding-top: 16px; padding-bottom: 16px;">
    <tr>
        <td style="font-family: 'Inter', Arial, Helvetica, sans-serif; font-size: 16px; line-height: 20px; font-weight: normal; mso-line-height-alt: 0px; mso-ansi-font-size: 0;" align="center">
            
            <!-- Button -->
            <!--[if mso]>
            <v:roundrect xmlns:v="urn:schemas-microsoft-com:vml" xmlns:w="urn:schemas-microsoft-com:office:word" href="https://www.capitalontap.com/" style="width:160px;height:40px;v-text-anchor:middle" arcsize="100%" fillcolor="#fdb728"  stroke="f">
            <v:textbox>
            <w:anchorlock></w:anchorlock>
            <center style="font-family: Arial, Helvetica, sans-serif; font-size: 16px; mso-line-height-alt: 20px; mso-text-raise: 1px; mso-line-height-rule: exactly; font-weight: normal; color: #000814">
            Learn more
            </center>
            </v:textbox>
            </v:roundrect>
            <![endif]-->
            <a href="https://www.capitalontap.com/" style="margin: 0; box-sizing: border-box; text-decoration: inherit; font-size: 16px; font-weight: normal; color: #000814; font-family: 'Inter', Arial, Helvetica, sans-serif; width: 160px; line-height: 20px; border-radius: 100px; background-color: #fdd051; background: linear-gradient(to bottom, #fdd051 0%,#fcae2a 100%); display: inline-block; text-align: center; padding: 10px; mso-hide: all;">
            Learn more
            </a>
            <!-- END Button -->
            
        </td>
    </tr>
  </table>
<!-- END Centred Button -->
```

### Signature Text

![Screenshot 2024-12-06 at 12.03.05.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/c3300230-0f49-45f5-a5ac-64f980a38bad/7ec4051c-7e0a-4337-994e-f0429b7e7827/Screenshot_2024-12-06_at_12.03.05.png)

**Purpose:** To conclude the email with a professional closing, including sender details and optional social media links, ensuring the recipient knows how to reach out for further assistance.

```html
<!-- Signature Text -->
<table width="100%" border="0" cellspacing="0" cellpadding="0" style="padding-top: 16px; padding-bottom: 16px;">
<tr>
    <td style="font-family: 'Inter', Arial, sans-serif; font-size: 16px; line-height: 28px; color: #4D525B; text-align: left;">
        Best wishes,<br />
        <strong style="font-family: 'Epilogue', Arial, sans-serif; color: #000814;">Capital on Tap</strong>
    </td>
</tr>
</table>
<!-- END Signature Text -->
```

### Inline Link

Purpose: Hyperlinks within the email's text, allowing recipients to complete actions without disrupting the flow of the content. Using this specific link style ensures it’s displayed correctly across browsers and email clients.

```html
<a href="[Replace with your URL]" target="_blank" class="link-u c-blue" style="text-decoration:underline; color:#2B4DC7;"><span class="link-u c-blue" style="text-decoration:underline; color:#2B4DC7;">This is an inline link</span></a>
```

[Email Template Generator Prompt](https://www.notion.so/Email-Template-Generator-Prompt-15aea9fc06d18013bad9d0e002b49ea2?pvs=21)