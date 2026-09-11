from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='0a4dbd51-9a02-56a3-8fb5-cfd7886164de',
    key='SV035',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Koffing.Name',
    display_name='Koffing',
    searchable_by=['Koffing', 'Basic', 'Koffing'],
    subtypes=['Basic'],
    collector_number=109,
    set_code='SV035',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=109,
    abilities=[
        Attack(
            title='Suspicious Gas',
            game_text="Your opponent's Active Pokémon is now Confused.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            effect=standard_attack,
        ),
    ],
)
