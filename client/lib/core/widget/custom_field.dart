import 'package:client/core/theme/app_pallete.dart';
import 'package:flutter/material.dart';

class CustomField extends StatelessWidget {
  final String hintText;
  final VoidCallback? onTap;
  final TextEditingController controller;
  final bool readOnly;
  final bool isObscureText;

  const CustomField({
    super.key,
    required this.hintText,
    required this.controller,
    this.readOnly = false,
    this.isObscureText = false,
    this.onTap,
  });

  @override
  Widget build(BuildContext context) {
    return TextFormField(
      decoration: InputDecoration(
        hintText: hintText,
        hintStyle: TextStyle(color: Pallete.greyColor),
      ),
      onTap: onTap,
      readOnly: readOnly,
      controller: controller,
      obscureText: isObscureText,
      validator: (val) {
        if (val!.trim().isEmpty) {
          return "$hintText is missing";
        }
        return null;
      },
    );
  }
}
