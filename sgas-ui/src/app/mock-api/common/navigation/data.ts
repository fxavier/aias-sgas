/* eslint-disable */
import { FuseNavigationItem } from '@fuse/components/navigation';


export const defaultNavigation: FuseNavigationItem[] = [
    {
        id: 'dashboards',
        title: 'Dashboards',
        subtitle: 'Unique dashboard designs',
        type: 'group',
        icon: 'heroicons_outline:home',
        children: [
            {
                id: 'dashboards.project',
                title: 'Project',
                type: 'basic',
                icon: 'heroicons_outline:clipboard-document-check',
                link: '/dashboards/project',
            },
            {
                id: 'dashboards.analytics',
                title: 'Analytics',
                type: 'basic',
                icon: 'heroicons_outline:chart-pie',
                link: '/dashboards/analytics',
            }
        ],
    },

    {
        id: 'modulos',
        title: 'Modulos',
        subtitle: 'Modulos do sistema',
        type: 'group',
        icon: 'heroicons_outline:rectangle-stack',
        children: [
          
            {
                id: 'user-interface.forms',
                title: 'Document management',
                type: 'collapsable',
                icon: 'heroicons_outline:pencil-square',
                children: [
                    {
                        id: 'user-interface.forms.fields',
                        title: 'Fields',
                        type: 'basic',
                        link: '/ui/forms/fields',
                    },
                    {
                        id: 'user-interface.forms.layouts',
                        title: 'Layouts',
                        type: 'basic',
                        link: '/ui/forms/layouts',
                    },
                    {
                        id: 'user-interface.forms.wizards',
                        title: 'Wizards',
                        type: 'basic',
                        link: '/ui/forms/wizards',
                    },
                ],
            },
            {
                id: 'user-interface.icons',
                title: 'Emergency Response',
                type: 'collapsable',
                icon: 'heroicons_outline:bolt',
                children: [
                    {
                        id: 'user-interface.icons.heroicons-outline',
                        title: 'Heroicons Outline',
                        type: 'basic',
                        link: '/ui/icons/heroicons-outline',
                    },
                    {
                        id: 'user-interface.icons.heroicons-solid',
                        title: 'Heroicons Solid',
                        type: 'basic',
                        link: '/ui/icons/heroicons-solid',
                    },
                    {
                        id: 'user-interface.icons.heroicons-mini',
                        title: 'Heroicons Mini',
                        type: 'basic',
                        link: '/ui/icons/heroicons-mini',
                    },
                    {
                        id: 'user-interface.icons.material-twotone',
                        title: 'Material Twotone',
                        type: 'basic',
                        link: '/ui/icons/material-twotone',
                    },
                    {
                        id: 'user-interface.icons.material-outline',
                        title: 'Material Outline',
                        type: 'basic',
                        link: '/ui/icons/material-outline',
                    },
                    {
                        id: 'user-interface.icons.material-solid',
                        title: 'Material Solid',
                        type: 'basic',
                        link: '/ui/icons/material-solid',
                    },
                    {
                        id: 'user-interface.icons.feather',
                        title: 'Feather',
                        type: 'basic',
                        link: '/ui/icons/feather',
                    },
                ],
            },
            
            {
                id: 'user-interface.page-layouts',
                title: 'Grievance Mechanism',
                type: 'collapsable',
                icon: 'heroicons_outline:rectangle-group',
                children: [
                    {
                        id: 'user-interface.page-layouts.overview',
                        title: 'Overview',
                        type: 'basic',
                        link: '/ui/page-layouts/overview',
                    },
                    {
                        id: 'user-interface.page-layouts.empty',
                        title: 'Empty',
                        type: 'basic',
                        link: '/ui/page-layouts/empty',
                    },
                    {
                        id: 'user-interface.page-layouts.carded',

                        title: 'Carded',
                        type: 'collapsable',
                        children: [
                            {
                                id: 'user-interface.page-layouts.carded.fullwidth',
                                title: 'Fullwidth',
                                type: 'basic',
                                link: '/ui/page-layouts/carded/fullwidth',
                            },
                            {
                                id: 'user-interface.page-layouts.carded.left-sidebar-1',
                                title: 'Left Sidebar #1',
                                type: 'basic',
                                link: '/ui/page-layouts/carded/left-sidebar-1',
                            },
                            {
                                id: 'user-interface.page-layouts.carded.left-sidebar-2',
                                title: 'Left Sidebar #2',
                                type: 'basic',
                                link: '/ui/page-layouts/carded/left-sidebar-2',
                            },
                            {
                                id: 'user-interface.page-layouts.carded.right-sidebar-1',
                                title: 'Right Sidebar #1',
                                type: 'basic',
                                link: '/ui/page-layouts/carded/right-sidebar-1',
                            },
                            {
                                id: 'user-interface.page-layouts.carded.right-sidebar-2',
                                title: 'Right Sidebar #2',
                                type: 'basic',
                                link: '/ui/page-layouts/carded/right-sidebar-2',
                            },
                        ],
                    },
                    {
                        id: 'user-interface.page-layouts.simple',
                        title: 'Simple',
                        type: 'collapsable',
                        children: [
                            {
                                id: 'user-interface.page-layouts.simple.fullwidth-1',
                                title: 'Fullwidth #1',
                                type: 'basic',
                                link: '/ui/page-layouts/simple/fullwidth-1',
                            },
                            {
                                id: 'user-interface.page-layouts.simple.fullwidth-2',
                                title: 'Fullwidth #2',
                                type: 'basic',
                                link: '/ui/page-layouts/simple/fullwidth-2',
                            },
                            {
                                id: 'user-interface.page-layouts.simple.left-sidebar-1',
                                title: 'Left Sidebar #1',
                                type: 'basic',
                                link: '/ui/page-layouts/simple/left-sidebar-1',
                            },
                            {
                                id: 'user-interface.page-layouts.simple.left-sidebar-2',
                                title: 'Left Sidebar #2',
                                type: 'basic',
                                link: '/ui/page-layouts/simple/left-sidebar-2',
                            },
                            {
                                id: 'user-interface.page-layouts.simple.left-sidebar-3',
                                title: 'Left Sidebar #3',
                                type: 'basic',
                                link: '/ui/page-layouts/simple/left-sidebar-3',
                            },
                            {
                                id: 'user-interface.page-layouts.simple.right-sidebar-1',
                                title: 'Right Sidebar #1',
                                type: 'basic',
                                link: '/ui/page-layouts/simple/right-sidebar-1',
                            },
                            {
                                id: 'user-interface.page-layouts.simple.right-sidebar-2',
                                title: 'Right Sidebar #2',
                                type: 'basic',
                                link: '/ui/page-layouts/simple/right-sidebar-2',
                            },
                            {
                                id: 'user-interface.page-layouts.simple.right-sidebar-3',
                                title: 'Right Sidebar #3',
                                type: 'basic',
                                link: '/ui/page-layouts/simple/right-sidebar-3',
                            },
                        ],
                    },
                ],
            },
            {
                id: 'user-interface.page-layouts',
                title: 'Grievance Mechanism',
                type: 'collapsable',
                icon: 'heroicons_outline:rectangle-group',
                children: [
                    {
                        id: 'user-interface.page-layouts.overview',
                        title: 'Overview',
                        type: 'basic',
                        link: '/ui/page-layouts/overview',
                    },
                    {
                        id: 'user-interface.page-layouts.empty',
                        title: 'Empty',
                        type: 'basic',
                        link: '/ui/page-layouts/empty',
                    },
                    {
                        id: 'user-interface.page-layouts.carded',

                        title: 'Carded',
                        type: 'collapsable',
                        children: [
                            {
                                id: 'user-interface.page-layouts.carded.fullwidth',
                                title: 'Fullwidth',
                                type: 'basic',
                                link: '/ui/page-layouts/carded/fullwidth',
                            },
                            {
                                id: 'user-interface.page-layouts.carded.left-sidebar-1',
                                title: 'Left Sidebar #1',
                                type: 'basic',
                                link: '/ui/page-layouts/carded/left-sidebar-1',
                            },
                            {
                                id: 'user-interface.page-layouts.carded.left-sidebar-2',
                                title: 'Left Sidebar #2',
                                type: 'basic',
                                link: '/ui/page-layouts/carded/left-sidebar-2',
                            },
                            {
                                id: 'user-interface.page-layouts.carded.right-sidebar-1',
                                title: 'Right Sidebar #1',
                                type: 'basic',
                                link: '/ui/page-layouts/carded/right-sidebar-1',
                            },
                            {
                                id: 'user-interface.page-layouts.carded.right-sidebar-2',
                                title: 'Right Sidebar #2',
                                type: 'basic',
                                link: '/ui/page-layouts/carded/right-sidebar-2',
                            },
                        ],
                    },
                    {
                        id: 'user-interface.page-layouts.simple',
                        title: 'Simple',
                        type: 'collapsable',
                        children: [
                            {
                                id: 'user-interface.page-layouts.simple.fullwidth-1',
                                title: 'Fullwidth #1',
                                type: 'basic',
                                link: '/ui/page-layouts/simple/fullwidth-1',
                            },
                            {
                                id: 'user-interface.page-layouts.simple.fullwidth-2',
                                title: 'Fullwidth #2',
                                type: 'basic',
                                link: '/ui/page-layouts/simple/fullwidth-2',
                            },
                            {
                                id: 'user-interface.page-layouts.simple.left-sidebar-1',
                                title: 'Left Sidebar #1',
                                type: 'basic',
                                link: '/ui/page-layouts/simple/left-sidebar-1',
                            },
                            {
                                id: 'user-interface.page-layouts.simple.left-sidebar-2',
                                title: 'Left Sidebar #2',
                                type: 'basic',
                                link: '/ui/page-layouts/simple/left-sidebar-2',
                            },
                            {
                                id: 'user-interface.page-layouts.simple.left-sidebar-3',
                                title: 'Left Sidebar #3',
                                type: 'basic',
                                link: '/ui/page-layouts/simple/left-sidebar-3',
                            },
                            {
                                id: 'user-interface.page-layouts.simple.right-sidebar-1',
                                title: 'Right Sidebar #1',
                                type: 'basic',
                                link: '/ui/page-layouts/simple/right-sidebar-1',
                            },
                            {
                                id: 'user-interface.page-layouts.simple.right-sidebar-2',
                                title: 'Right Sidebar #2',
                                type: 'basic',
                                link: '/ui/page-layouts/simple/right-sidebar-2',
                            },
                            {
                                id: 'user-interface.page-layouts.simple.right-sidebar-3',
                                title: 'Right Sidebar #3',
                                type: 'basic',
                                link: '/ui/page-layouts/simple/right-sidebar-3',
                            },
                        ],
                    },
                ],
            },
            {
                id: 'user-interface.page-layouts',
                title: 'Grievance Mechanism',
                type: 'collapsable',
                icon: 'heroicons_outline:rectangle-group',
                children: [
                    {
                        id: 'user-interface.page-layouts.overview',
                        title: 'Overview',
                        type: 'basic',
                        link: '/ui/page-layouts/overview',
                    },
                    {
                        id: 'user-interface.page-layouts.empty',
                        title: 'Empty',
                        type: 'basic',
                        link: '/ui/page-layouts/empty',
                    },
                    {
                        id: 'user-interface.page-layouts.carded',

                        title: 'Carded',
                        type: 'collapsable',
                        children: [
                            {
                                id: 'user-interface.page-layouts.carded.fullwidth',
                                title: 'Fullwidth',
                                type: 'basic',
                                link: '/ui/page-layouts/carded/fullwidth',
                            },
                            {
                                id: 'user-interface.page-layouts.carded.left-sidebar-1',
                                title: 'Left Sidebar #1',
                                type: 'basic',
                                link: '/ui/page-layouts/carded/left-sidebar-1',
                            },
                            {
                                id: 'user-interface.page-layouts.carded.left-sidebar-2',
                                title: 'Left Sidebar #2',
                                type: 'basic',
                                link: '/ui/page-layouts/carded/left-sidebar-2',
                            },
                            {
                                id: 'user-interface.page-layouts.carded.right-sidebar-1',
                                title: 'Right Sidebar #1',
                                type: 'basic',
                                link: '/ui/page-layouts/carded/right-sidebar-1',
                            },
                            {
                                id: 'user-interface.page-layouts.carded.right-sidebar-2',
                                title: 'Right Sidebar #2',
                                type: 'basic',
                                link: '/ui/page-layouts/carded/right-sidebar-2',
                            },
                        ],
                    },
                    {
                        id: 'user-interface.page-layouts.simple',
                        title: 'Simple',
                        type: 'collapsable',
                        children: [
                            {
                                id: 'user-interface.page-layouts.simple.fullwidth-1',
                                title: 'Fullwidth #1',
                                type: 'basic',
                                link: '/ui/page-layouts/simple/fullwidth-1',
                            },
                            {
                                id: 'user-interface.page-layouts.simple.fullwidth-2',
                                title: 'Fullwidth #2',
                                type: 'basic',
                                link: '/ui/page-layouts/simple/fullwidth-2',
                            },
                            {
                                id: 'user-interface.page-layouts.simple.left-sidebar-1',
                                title: 'Left Sidebar #1',
                                type: 'basic',
                                link: '/ui/page-layouts/simple/left-sidebar-1',
                            },
                            {
                                id: 'user-interface.page-layouts.simple.left-sidebar-2',
                                title: 'Left Sidebar #2',
                                type: 'basic',
                                link: '/ui/page-layouts/simple/left-sidebar-2',
                            },
                            {
                                id: 'user-interface.page-layouts.simple.left-sidebar-3',
                                title: 'Left Sidebar #3',
                                type: 'basic',
                                link: '/ui/page-layouts/simple/left-sidebar-3',
                            },
                            {
                                id: 'user-interface.page-layouts.simple.right-sidebar-1',
                                title: 'Right Sidebar #1',
                                type: 'basic',
                                link: '/ui/page-layouts/simple/right-sidebar-1',
                            },
                            {
                                id: 'user-interface.page-layouts.simple.right-sidebar-2',
                                title: 'Right Sidebar #2',
                                type: 'basic',
                                link: '/ui/page-layouts/simple/right-sidebar-2',
                            },
                            {
                                id: 'user-interface.page-layouts.simple.right-sidebar-3',
                                title: 'Right Sidebar #3',
                                type: 'basic',
                                link: '/ui/page-layouts/simple/right-sidebar-3',
                            },
                        ],
                    },
                ],
            },
            {
                id: 'user-interface.page-layouts',
                title: 'Grievance Mechanism',
                type: 'collapsable',
                icon: 'heroicons_outline:rectangle-group',
                children: [
                    {
                        id: 'user-interface.page-layouts.overview',
                        title: 'Overview',
                        type: 'basic',
                        link: '/ui/page-layouts/overview',
                    },
                    {
                        id: 'user-interface.page-layouts.empty',
                        title: 'Empty',
                        type: 'basic',
                        link: '/ui/page-layouts/empty',
                    },
                    {
                        id: 'user-interface.page-layouts.carded',

                        title: 'Carded',
                        type: 'collapsable',
                        children: [
                            {
                                id: 'user-interface.page-layouts.carded.fullwidth',
                                title: 'Fullwidth',
                                type: 'basic',
                                link: '/ui/page-layouts/carded/fullwidth',
                            },
                            {
                                id: 'user-interface.page-layouts.carded.left-sidebar-1',
                                title: 'Left Sidebar #1',
                                type: 'basic',
                                link: '/ui/page-layouts/carded/left-sidebar-1',
                            },
                            {
                                id: 'user-interface.page-layouts.carded.left-sidebar-2',
                                title: 'Left Sidebar #2',
                                type: 'basic',
                                link: '/ui/page-layouts/carded/left-sidebar-2',
                            },
                            {
                                id: 'user-interface.page-layouts.carded.right-sidebar-1',
                                title: 'Right Sidebar #1',
                                type: 'basic',
                                link: '/ui/page-layouts/carded/right-sidebar-1',
                            },
                            {
                                id: 'user-interface.page-layouts.carded.right-sidebar-2',
                                title: 'Right Sidebar #2',
                                type: 'basic',
                                link: '/ui/page-layouts/carded/right-sidebar-2',
                            },
                        ],
                    },
                    {
                        id: 'user-interface.page-layouts.simple',
                        title: 'Simple',
                        type: 'collapsable',
                        children: [
                            {
                                id: 'user-interface.page-layouts.simple.fullwidth-1',
                                title: 'Fullwidth #1',
                                type: 'basic',
                                link: '/ui/page-layouts/simple/fullwidth-1',
                            },
                            {
                                id: 'user-interface.page-layouts.simple.fullwidth-2',
                                title: 'Fullwidth #2',
                                type: 'basic',
                                link: '/ui/page-layouts/simple/fullwidth-2',
                            },
                            {
                                id: 'user-interface.page-layouts.simple.left-sidebar-1',
                                title: 'Left Sidebar #1',
                                type: 'basic',
                                link: '/ui/page-layouts/simple/left-sidebar-1',
                            },
                            {
                                id: 'user-interface.page-layouts.simple.left-sidebar-2',
                                title: 'Left Sidebar #2',
                                type: 'basic',
                                link: '/ui/page-layouts/simple/left-sidebar-2',
                            },
                            {
                                id: 'user-interface.page-layouts.simple.left-sidebar-3',
                                title: 'Left Sidebar #3',
                                type: 'basic',
                                link: '/ui/page-layouts/simple/left-sidebar-3',
                            },
                            {
                                id: 'user-interface.page-layouts.simple.right-sidebar-1',
                                title: 'Right Sidebar #1',
                                type: 'basic',
                                link: '/ui/page-layouts/simple/right-sidebar-1',
                            },
                            {
                                id: 'user-interface.page-layouts.simple.right-sidebar-2',
                                title: 'Right Sidebar #2',
                                type: 'basic',
                                link: '/ui/page-layouts/simple/right-sidebar-2',
                            },
                            {
                                id: 'user-interface.page-layouts.simple.right-sidebar-3',
                                title: 'Right Sidebar #3',
                                type: 'basic',
                                link: '/ui/page-layouts/simple/right-sidebar-3',
                            },
                        ],
                    },
                ],
            },
            {
                id: 'user-interface.page-layouts',
                title: 'Grievance Mechanism',
                type: 'collapsable',
                icon: 'heroicons_outline:rectangle-group',
                children: [
                    {
                        id: 'user-interface.page-layouts.overview',
                        title: 'Overview',
                        type: 'basic',
                        link: '/ui/page-layouts/overview',
                    },
                    {
                        id: 'user-interface.page-layouts.empty',
                        title: 'Empty',
                        type: 'basic',
                        link: '/ui/page-layouts/empty',
                    },
                    {
                        id: 'user-interface.page-layouts.carded',

                        title: 'Carded',
                        type: 'collapsable',
                        children: [
                            {
                                id: 'user-interface.page-layouts.carded.fullwidth',
                                title: 'Fullwidth',
                                type: 'basic',
                                link: '/ui/page-layouts/carded/fullwidth',
                            },
                            {
                                id: 'user-interface.page-layouts.carded.left-sidebar-1',
                                title: 'Left Sidebar #1',
                                type: 'basic',
                                link: '/ui/page-layouts/carded/left-sidebar-1',
                            },
                            {
                                id: 'user-interface.page-layouts.carded.left-sidebar-2',
                                title: 'Left Sidebar #2',
                                type: 'basic',
                                link: '/ui/page-layouts/carded/left-sidebar-2',
                            },
                            {
                                id: 'user-interface.page-layouts.carded.right-sidebar-1',
                                title: 'Right Sidebar #1',
                                type: 'basic',
                                link: '/ui/page-layouts/carded/right-sidebar-1',
                            },
                            {
                                id: 'user-interface.page-layouts.carded.right-sidebar-2',
                                title: 'Right Sidebar #2',
                                type: 'basic',
                                link: '/ui/page-layouts/carded/right-sidebar-2',
                            },
                        ],
                    },
                    {
                        id: 'user-interface.page-layouts.simple',
                        title: 'Simple',
                        type: 'collapsable',
                        children: [
                            {
                                id: 'user-interface.page-layouts.simple.fullwidth-1',
                                title: 'Fullwidth #1',
                                type: 'basic',
                                link: '/ui/page-layouts/simple/fullwidth-1',
                            },
                            {
                                id: 'user-interface.page-layouts.simple.fullwidth-2',
                                title: 'Fullwidth #2',
                                type: 'basic',
                                link: '/ui/page-layouts/simple/fullwidth-2',
                            },
                            {
                                id: 'user-interface.page-layouts.simple.left-sidebar-1',
                                title: 'Left Sidebar #1',
                                type: 'basic',
                                link: '/ui/page-layouts/simple/left-sidebar-1',
                            },
                            {
                                id: 'user-interface.page-layouts.simple.left-sidebar-2',
                                title: 'Left Sidebar #2',
                                type: 'basic',
                                link: '/ui/page-layouts/simple/left-sidebar-2',
                            },
                            {
                                id: 'user-interface.page-layouts.simple.left-sidebar-3',
                                title: 'Left Sidebar #3',
                                type: 'basic',
                                link: '/ui/page-layouts/simple/left-sidebar-3',
                            },
                            {
                                id: 'user-interface.page-layouts.simple.right-sidebar-1',
                                title: 'Right Sidebar #1',
                                type: 'basic',
                                link: '/ui/page-layouts/simple/right-sidebar-1',
                            },
                            {
                                id: 'user-interface.page-layouts.simple.right-sidebar-2',
                                title: 'Right Sidebar #2',
                                type: 'basic',
                                link: '/ui/page-layouts/simple/right-sidebar-2',
                            },
                            {
                                id: 'user-interface.page-layouts.simple.right-sidebar-3',
                                title: 'Right Sidebar #3',
                                type: 'basic',
                                link: '/ui/page-layouts/simple/right-sidebar-3',
                            },
                        ],
                    },
                ],
            },
            {
                id: 'user-interface.page-layouts',
                title: 'Risks and Impact',
                type: 'collapsable',
                icon: 'heroicons_outline:rectangle-group',
                children: [
                    {
                        id: 'user-interface.page-layouts.overview',
                        title: 'Evironment & Social Risk impact Assessment',
                        type: 'basic',
                        link: '/add-env-social-risk-impact-assessement',
                    },
                    {
                        id: 'user-interface.page-layouts.empty',
                        title: 'Empty',
                        type: 'basic',
                        link: '/ui/page-layouts/empty',
                    },
                    {
                        id: 'user-interface.page-layouts.carded',

                        title: 'Carded',
                        type: 'collapsable',
                        children: [
                            {
                                id: 'user-interface.page-layouts.carded.fullwidth',
                                title: 'Fullwidth',
                                type: 'basic',
                                link: '/ui/page-layouts/carded/fullwidth',
                            },
                            {
                                id: 'user-interface.page-layouts.carded.left-sidebar-1',
                                title: 'Left Sidebar #1',
                                type: 'basic',
                                link: '/ui/page-layouts/carded/left-sidebar-1',
                            },
                            {
                                id: 'user-interface.page-layouts.carded.left-sidebar-2',
                                title: 'Left Sidebar #2',
                                type: 'basic',
                                link: '/ui/page-layouts/carded/left-sidebar-2',
                            },
                            {
                                id: 'user-interface.page-layouts.carded.right-sidebar-1',
                                title: 'Right Sidebar #1',
                                type: 'basic',
                                link: '/ui/page-layouts/carded/right-sidebar-1',
                            },
                            {
                                id: 'user-interface.page-layouts.carded.right-sidebar-2',
                                title: 'Right Sidebar #2',
                                type: 'basic',
                                link: '/ui/page-layouts/carded/right-sidebar-2',
                            },
                        ],
                    },
                    {
                        id: 'user-interface.page-layouts.simple',
                        title: 'Simple',
                        type: 'collapsable',
                        children: [
                            {
                                id: 'user-interface.page-layouts.simple.fullwidth-1',
                                title: 'Fullwidth #1',
                                type: 'basic',
                                link: '/ui/page-layouts/simple/fullwidth-1',
                            },
                            {
                                id: 'user-interface.page-layouts.simple.fullwidth-2',
                                title: 'Fullwidth #2',
                                type: 'basic',
                                link: '/ui/page-layouts/simple/fullwidth-2',
                            },
                            {
                                id: 'user-interface.page-layouts.simple.left-sidebar-1',
                                title: 'Left Sidebar #1',
                                type: 'basic',
                                link: '/ui/page-layouts/simple/left-sidebar-1',
                            },
                            {
                                id: 'user-interface.page-layouts.simple.left-sidebar-2',
                                title: 'Left Sidebar #2',
                                type: 'basic',
                                link: '/ui/page-layouts/simple/left-sidebar-2',
                            },
                            {
                                id: 'user-interface.page-layouts.simple.left-sidebar-3',
                                title: 'Left Sidebar #3',
                                type: 'basic',
                                link: '/ui/page-layouts/simple/left-sidebar-3',
                            },
                            {
                                id: 'user-interface.page-layouts.simple.right-sidebar-1',
                                title: 'Right Sidebar #1',
                                type: 'basic',
                                link: '/ui/page-layouts/simple/right-sidebar-1',
                            },
                            {
                                id: 'user-interface.page-layouts.simple.right-sidebar-2',
                                title: 'Right Sidebar #2',
                                type: 'basic',
                                link: '/ui/page-layouts/simple/right-sidebar-2',
                            },
                            {
                                id: 'user-interface.page-layouts.simple.right-sidebar-3',
                                title: 'Right Sidebar #3',
                                type: 'basic',
                                link: '/ui/page-layouts/simple/right-sidebar-3',
                            },
                        ],
                    },
                ],
            },
            
        ],
    }
];
export const compactNavigation: FuseNavigationItem[] = [
    {
        id: 'dashboards',
        title: 'Dashboards',
        tooltip: 'Dashboards',
        type: 'aside',
        icon: 'heroicons_outline:home',
        children: [], // This will be filled from defaultNavigation so we don't have to manage multiple sets of the same navigation
    },
    {
        id: 'apps',
        title: 'Apps',
        tooltip: 'Apps',
        type: 'aside',
        icon: 'heroicons_outline:squares-2x2',
        children: [], // This will be filled from defaultNavigation so we don't have to manage multiple sets of the same navigation
    },
    {
        id: 'pages',
        title: 'Pages',
        tooltip: 'Pages',
        type: 'aside',
        icon: 'heroicons_outline:document-duplicate',
        children: [], // This will be filled from defaultNavigation so we don't have to manage multiple sets of the same navigation
    },
    {
        id: 'user-interface',
        title: 'UI',
        tooltip: 'UI',
        type: 'aside',
        icon: 'heroicons_outline:rectangle-stack',
        children: [], // This will be filled from defaultNavigation so we don't have to manage multiple sets of the same navigation
    },
    {
        id: 'navigation-features',
        title: 'Navigation',
        tooltip: 'Navigation',
        type: 'aside',
        icon: 'heroicons_outline:bars-3',
        children: [], // This will be filled from defaultNavigation so we don't have to manage multiple sets of the same navigation
    },
];
export const futuristicNavigation: FuseNavigationItem[] = [
    {
        id: 'dashboards',
        title: 'DASHBOARDS',
        type: 'group',
        children: [], // This will be filled from defaultNavigation so we don't have to manage multiple sets of the same navigation
    },
    {
        id: 'apps',
        title: 'APPS',
        type: 'group',
        children: [], // This will be filled from defaultNavigation so we don't have to manage multiple sets of the same navigation
    },
    {
        id: 'others',
        title: 'OTHERS',
        type: 'group',
    },
    {
        id: 'pages',
        title: 'Pages',
        type: 'aside',
        icon: 'heroicons_outline:document-duplicate',
        children: [], // This will be filled from defaultNavigation so we don't have to manage multiple sets of the same navigation
    },
    {
        id: 'user-interface',
        title: 'User Interface',
        type: 'aside',
        icon: 'heroicons_outline:rectangle-stack',
        children: [], // This will be filled from defaultNavigation so we don't have to manage multiple sets of the same navigation
    },
    {
        id: 'navigation-features',
        title: 'Navigation Features',
        type: 'aside',
        icon: 'heroicons_outline:bars-3',
        children: [], // This will be filled from defaultNavigation so we don't have to manage multiple sets of the same navigation
    },
];
export const horizontalNavigation: FuseNavigationItem[] = [
    {
        id: 'dashboards',
        title: 'Dashboards',
        type: 'group',
        icon: 'heroicons_outline:home',
        children: [], // This will be filled from defaultNavigation so we don't have to manage multiple sets of the same navigation
    },
    {
        id: 'apps',
        title: 'Apps',
        type: 'group',
        icon: 'heroicons_outline:squares-2x2',
        children: [], // This will be filled from defaultNavigation so we don't have to manage multiple sets of the same navigation
    },
    {
        id: 'pages',
        title: 'Pages',
        type: 'group',
        icon: 'heroicons_outline:document-duplicate',
        children: [], // This will be filled from defaultNavigation so we don't have to manage multiple sets of the same navigation
    },
    {
        id: 'user-interface',
        title: 'UI',
        type: 'group',
        icon: 'heroicons_outline:rectangle-stack',
        children: [], // This will be filled from defaultNavigation so we don't have to manage multiple sets of the same navigation
    },
    {
        id: 'navigation-features',
        title: 'Misc',
        type: 'group',
        icon: 'heroicons_outline:bars-3',
        children: [], // This will be filled from defaultNavigation so we don't have to manage multiple sets of the same navigation
    },
];
