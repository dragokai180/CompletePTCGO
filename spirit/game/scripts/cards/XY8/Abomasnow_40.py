from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e1d6367b-0987-52d0-afc6-d69dbffbaf8e',
    key='XY8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Abomasnow.Name',
    display_name='Abomasnow',
    searchable_by=['Abomasnow', 'Stage 1', 'Abomasnow'],
    subtypes=['Stage 1'],
    collector_number=40,
    set_code='XY8',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Snover.Name',
    family_id=459,
    abilities=[
        Attack(
            title='Ice Age',
            game_text="If your opponent's Active Pokémon is a Dragon Pokémon, it is now Paralyzed.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            effect=standard_attack,
        ),
        Attack(
            title='Frost Breath',
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 2},
            damage=110,
        ),
    ],
)
