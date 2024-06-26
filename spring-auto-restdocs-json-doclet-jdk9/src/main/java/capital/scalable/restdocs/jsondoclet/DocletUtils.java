/*-
 * #%L
 * Spring Auto REST Docs Json Doclet for JDK9+
 * %%
 * Copyright (C) 2015 - 2024 Scalable Capital GmbH
 * %%
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 * #L%
 */
package capital.scalable.restdocs.jsondoclet;

import java.util.Optional;

public class DocletUtils {
    private DocletUtils() {
        // utils
    }

    static String cleanupDocComment(String comment) {
        return Optional.ofNullable(comment).map(s -> s.replaceAll("(?:^|[\\r\\n]+)\\s*@.*", "").trim()).orElse("");
    }

    public static String cleanupTagValue(String value) {
        return value.replaceFirst("\\s*@[^\\s]+\\s+", "").trim();
    }

    public static String cleanupTagName(String name) {
        return name.startsWith("@") ? name.substring(1) : name;
    }

}
