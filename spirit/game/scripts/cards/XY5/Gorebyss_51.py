from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='35546c18-1feb-568e-8126-887f1f68b627',
    key='XY5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Gorebyss.Name',
    display_name='Gorebyss',
    searchable_by=['Gorebyss', 'Stage 1', 'Gorebyss'],
    subtypes=['Stage 1'],
    collector_number=51,
    set_code='XY5',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Clamperl.Name',
    family_id=366,
    abilities=[
        Attack(
            title='Captivate',
            game_text="Switch 1 of your opponent's Benched Pokémon with his or her Active Pokémon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Psychic',
            game_text="This attack does 10 more damage for each Energy attached to your opponent's Active Pokémon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
