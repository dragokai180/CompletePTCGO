from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='7c88e153-5f01-55f1-abd1-797a76b8c2f1',
    key='XY9',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Drapion.Name',
    display_name='Drapion',
    searchable_by=['Drapion', 'Stage 1', 'Drapion'],
    subtypes=['Stage 1'],
    collector_number=54,
    set_code='XY9',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Skorupi.Name',
    family_id=451,
    abilities=[
        Attack(
            title='Poison Claws',
            game_text="Your opponent's Active Pokémon is now Poisoned.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=70,
            effect=standard_attack,
        ),
        Attack(
            title='Heavy Impact',
            cost={PokemonTypes.PSYCHIC: 3, PokemonTypes.COLORLESS: 1},
            damage=130,
        ),
    ],
)
