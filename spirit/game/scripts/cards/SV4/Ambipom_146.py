from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='da79aaef-e43e-59ff-b6a3-39eb2797b5d2',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Ambipom.Name',
    display_name='Ambipom',
    searchable_by=['Ambipom', 'Stage 1', 'Ambipom'],
    subtypes=['Stage 1'],
    collector_number=146,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Aipom.Name',
    family_id=190,
    abilities=[
        Attack(
            title='Collect',
            game_text='Draw 2 cards.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Hand Fling',
            game_text='This attack does 20 damage for each card in your hand.',
            cost={PokemonTypes.COLORLESS: 3},
            damage=20,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
