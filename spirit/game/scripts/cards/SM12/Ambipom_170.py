from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='06a4136a-20ad-5ba1-86bd-e12e9fc0468f',
    key='SM12',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Ambipom.Name',
    display_name='Ambipom',
    searchable_by=['Ambipom', 'Stage 1', 'Ambipom'],
    subtypes=['Stage 1'],
    collector_number=170,
    set_code='SM12',
    regulation_mark=None,
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
            title='Nice-Nice Catch',
            game_text='Draw 2 cards.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Bye-Bye Throw',
            game_text='Discard up to 2 cards from your hand. This attack does 60 damage for each card you discarded in this way.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
