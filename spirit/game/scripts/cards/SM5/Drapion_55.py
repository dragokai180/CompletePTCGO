from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='047eb8eb-d88d-586b-bd41-6a7207604b9c',
    key='SM5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Drapion.Name',
    display_name='Drapion',
    searchable_by=['Drapion', 'Stage 1', 'Drapion'],
    subtypes=['Stage 1'],
    collector_number=55,
    set_code='SM5',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Skorupi.Name',
    family_id=451,
    abilities=[
        Attack(
            title='Dangerous Stinger',
            game_text="Your opponent's Active Pokémon is now Paralyzed and Poisoned.",
            cost={PokemonTypes.PSYCHIC: 4},
            damage=100,
            effect=standard_attack,
        ),
    ],
)
