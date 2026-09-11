from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='44dfe8a5-efb3-5b8f-b036-75632998c6be',
    key='HGSS2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Steelix.Name',
    display_name='Steelix',
    searchable_by=['Steelix', 'Stage 1', 'Steelix'],
    subtypes=['Stage 1'],
    collector_number=24,
    set_code='HGSS2',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Onix.Name',
    family_id=95,
    abilities=[
        Attack(
            title='Guard Press',
            game_text="During your opponent's next turn, any damage done to Steelix by attacks is reduced by 20 (after applying Weakness and Resistance).",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=standard_attack,
        ),
        Attack(
            title='Steel Swing',
            game_text='Flip 2 coins. This attack does 80 damage times the number of heads.',
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 2},
            damage=80,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
