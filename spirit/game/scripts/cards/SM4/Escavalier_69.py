from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='613a8daa-3797-579e-adab-554fed120ad1',
    key='SM4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Escavalier.Name',
    display_name='Escavalier',
    searchable_by=['Escavalier', 'Stage 1', 'Escavalier'],
    subtypes=['Stage 1'],
    collector_number=69,
    set_code='SM4',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Karrablast.Name',
    family_id=588,
    abilities=[
        Attack(
            title='Fury Attack',
            game_text='Flip 3 coins. This attack does 30 damage for each heads.',
            cost={PokemonTypes.METAL: 1},
            damage=30,
            damage_operator='x',
            effect=standard_attack,
        ),
        Attack(
            title='Iron Tackle',
            game_text='This Pokémon does 30 damage to itself.',
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
            effect=standard_attack,
        ),
    ],
)
