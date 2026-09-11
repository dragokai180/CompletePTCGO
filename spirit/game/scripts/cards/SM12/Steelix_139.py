from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='7eda475d-78f4-5b16-9695-cf0b0db2bf67',
    key='SM12',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Steelix.Name',
    display_name='Steelix',
    searchable_by=['Steelix', 'Stage 1', 'Steelix'],
    subtypes=['Stage 1'],
    collector_number=139,
    set_code='SM12',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=170,
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
            title='Thumping Fall',
            game_text='Discard any number of Pokémon with a Retreat Cost of exactly 4 from your hand. This attack does 50 damage for each card you discarded in this way.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator='x',
            effect=standard_attack,
        ),
        Attack(
            title='Iron Tail',
            game_text='Flip a coin until you get tails. This attack does 100 damage for each heads.',
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 3},
            damage=100,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
