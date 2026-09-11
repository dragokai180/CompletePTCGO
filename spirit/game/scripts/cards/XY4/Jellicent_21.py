from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='acad5162-543c-5d4d-91ce-af0a3ad00fb1',
    key='XY4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Jellicent.Name',
    display_name='Jellicent',
    searchable_by=['Jellicent', 'Stage 1', 'Jellicent'],
    subtypes=['Stage 1'],
    collector_number=21,
    set_code='XY4',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Frillish.Name',
    family_id=592,
    abilities=[
        Attack(
            title='Meddling',
            game_text="Attach 3 Energy cards from your opponent's discard pile to his or her Pokémon in any way you like.",
            cost={PokemonTypes.WATER: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Ensnaring Spray',
            game_text="This attack does 10 more damage for each Energy attached to your opponent's Active Pokémon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
