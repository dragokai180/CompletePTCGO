from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='b5fc9805-782e-5182-9164-f6c2a6dd8f1d',
    key='XY5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Azumarill.Name',
    display_name='Azumarill',
    searchable_by=['Azumarill', 'Stage 1', 'Azumarill'],
    subtypes=['Stage 1'],
    collector_number=103,
    set_code='XY5',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Marill.Name',
    family_id=183,
    abilities=[
        Attack(
            title='Bubble Beam',
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=standard_attack,
        ),
        Attack(
            title='Superpower',
            game_text='You may do 30 more damage. If you do, this Pokémon does 30 damage to itself.',
            cost={PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
