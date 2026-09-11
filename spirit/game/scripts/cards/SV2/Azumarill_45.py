from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='c62327b9-234f-58ad-ae56-2886d94a52b6',
    key='SV2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Azumarill.Name',
    display_name='Azumarill',
    searchable_by=['Azumarill', 'Stage 1', 'Azumarill'],
    subtypes=['Stage 1'],
    collector_number=45,
    set_code='SV2',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Marill.Name',
    family_id=183,
    abilities=[
        Attack(
            title='Bubble Drain',
            game_text='Heal 30 damage from this Pokémon.',
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=standard_attack,
        ),
        Attack(
            title='Slam',
            game_text='Flip 2 coins. This attack does 100 damage for each heads.',
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
