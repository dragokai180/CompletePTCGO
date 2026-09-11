from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='6c5d07eb-f8e8-5af8-b350-88af2ad7412e',
    key='HGSS1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Raichu.Name',
    display_name='Raichu',
    searchable_by=['Raichu', 'Stage 1', 'Raichu'],
    subtypes=['Stage 1'],
    collector_number=10,
    set_code='HGSS1',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Pikachu.Name',
    family_id=25,
    abilities=[
        Attack(
            title='Iron Tail',
            game_text='Flip a coin until you get tails. This attack does 30 damage times the number of heads.',
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator='x',
            effect=standard_attack,
        ),
        Attack(
            title='Thunderbolt',
            game_text='Discard all Energy attached to Raichu.',
            cost={PokemonTypes.LIGHTNING: 2},
            damage=100,
            effect=standard_attack,
        ),
    ],
)
