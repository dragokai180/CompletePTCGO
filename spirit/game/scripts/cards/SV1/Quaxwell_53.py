from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='92cbc515-2a94-52a0-b95c-43cba1935a99',
    key='SV1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Quaxwell.Name',
    display_name='Quaxwell',
    searchable_by=['Quaxwell', 'Stage 1', 'Quaxwell'],
    subtypes=['Stage 1'],
    collector_number=53,
    set_code='SV1',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Quaxly.Name',
    family_id=912,
    abilities=[
        Attack(
            title='Rain Splash',
            cost={PokemonTypes.WATER: 1},
            damage=20,
        ),
        Attack(
            title='Spiral Kick',
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
        ),
    ],
)
