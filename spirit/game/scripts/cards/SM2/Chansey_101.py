from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='064f57d5-923e-5691-a2f3-f6a1e64a07ea',
    key='SM2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Chansey.Name',
    display_name='Chansey',
    searchable_by=['Chansey', 'Basic', 'Chansey'],
    subtypes=['Basic'],
    collector_number=101,
    set_code='SM2',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=110,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=113,
    abilities=[
        Attack(
            title='Bind Wound',
            game_text='Flip a coin. If heads, heal 30 damage from 1 of your Pokémon.',
            cost={PokemonTypes.COLORLESS: 2},
            effect=standard_attack,
        ),
        Attack(
            title='Hammer In',
            cost={PokemonTypes.COLORLESS: 4},
            damage=80,
        ),
    ],
)
