from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='db33b810-b0cf-54d6-92a0-1d0f1fb22bd5',
    key='SV035',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Lapras.Name',
    display_name='Lapras',
    searchable_by=['Lapras', 'Basic', 'Lapras'],
    subtypes=['Basic'],
    collector_number=131,
    set_code='SV035',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    family_id=131,
    abilities=[
        Attack(
            title='Hop on My Back',
            game_text='Search your deck for up to 2 Pokémon, reveal them, and put them into your hand. Then, shuffle your deck.',
            cost={PokemonTypes.WATER: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Aqua Edge',
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
        ),
    ],
)
