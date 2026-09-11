from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='c6702441-1aad-54fa-b1f5-cfc5436876d3',
    key='SM12',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Marshadow.Name',
    display_name='Marshadow',
    searchable_by=['Marshadow', 'Basic', 'Marshadow'],
    subtypes=['Basic'],
    collector_number=103,
    set_code='SM12',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=802,
    abilities=[
        Attack(
            title='Shadow Imitation',
            game_text="Choose 1 of your opponent's Active Pokémon's non-GX attacks and use it as this attack.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            effect=standard_attack,
        ),
    ],
)
