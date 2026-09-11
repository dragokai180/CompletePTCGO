from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='cc93f760-fd18-50d3-9bc9-3f2981748bac',
    key='XY10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Kabutops.Name',
    display_name='Kabutops',
    searchable_by=['Kabutops', 'Stage 1', 'Kabutops'],
    subtypes=['Stage 1'],
    collector_number=39,
    set_code='XY10',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Kabuto.Name',
    family_id=140,
    abilities=[
        Attack(
            title='Cling',
            game_text="Heal from this Pokémon the same amount of damage you did to your opponent's Active Pokémon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=standard_attack,
        ),
        Attack(
            title='X-Scissor',
            game_text='Flip a coin. If heads, this attack does 60 more damage.',
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
