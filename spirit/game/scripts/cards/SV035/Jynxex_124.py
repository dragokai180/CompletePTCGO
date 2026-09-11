from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='122af92b-644d-5588-bff1-8e7e4efc933c',
    key='SV035',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Jynxex.Name',
    display_name='Jynx ex',
    searchable_by=['Jynx ex', 'Basic', 'ex', 'Jynxex'],
    subtypes=['Basic', 'ex'],
    collector_number=124,
    set_code='SV035',
    regulation_mark='G',
    rarity=Rarities.RareHoloEX,
    hp=200,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    family_id=124,
    abilities=[
        Attack(
            title='Heart-Stopping Kiss',
            game_text="If your opponent's Active Pokémon is Asleep, it is Knocked Out.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            effect=standard_attack,
        ),
        Attack(
            title='Icy Wind',
            game_text="Your opponent's Active Pokémon is now Asleep.",
            cost={PokemonTypes.WATER: 3},
            damage=120,
            effect=standard_attack,
        ),
    ],
)
