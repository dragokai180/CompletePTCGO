from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='93dc3e9c-f951-5d11-8ecf-e6777201c323',
    key='SM6',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Honedge.Name',
    display_name='Honedge',
    searchable_by=['Honedge', 'Basic', 'Honedge'],
    subtypes=['Basic'],
    collector_number=46,
    set_code='SM6',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=679,
    abilities=[
        Ability(
            title='Final Hour',
            game_text="If this Pokémon is your Active Pokémon and is Knocked Out by damage from an opponent's attack, put 3 damage counters on 1 of your opponent's Pokémon.",
            passive=standard_passive("If this Pokémon is your Active Pokémon and is Knocked Out by damage from an opponent's attack, put 3 damage counters on 1 of your opponent's Pokémon."),
        ),
        Attack(
            title='Slash',
            cost={PokemonTypes.PSYCHIC: 3},
            damage=50,
        ),
    ],
)
