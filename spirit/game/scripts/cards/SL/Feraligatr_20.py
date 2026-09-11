from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='0cfc80c4-fa7c-55e2-99da-8ff3d7247d26',
    key='SL',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Feraligatr.Name',
    display_name='Feraligatr',
    searchable_by=['Feraligatr', 'Stage 2', 'Feraligatr'],
    subtypes=['Stage 2'],
    collector_number=20,
    set_code='SL',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=160,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Croconaw.Name',
    family_id=158,
    abilities=[
        Attack(
            title='Crunch',
            game_text="Discard an Energy from your opponent's Active Pokémon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            effect=standard_attack,
        ),
        Attack(
            title='Hydro Splash',
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 3},
            damage=130,
        ),
    ],
)
