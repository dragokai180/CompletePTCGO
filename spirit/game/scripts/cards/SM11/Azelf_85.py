from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='2cec6bb3-513e-5a78-850b-b36d048e234c',
    key='SM11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Azelf.Name',
    display_name='Azelf',
    searchable_by=['Azelf', 'Basic', 'Azelf'],
    subtypes=['Basic'],
    collector_number=85,
    set_code='SM11',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=482,
    abilities=[
        Attack(
            title='Psypower',
            game_text="Put 3 damage counters on your opponent's Pokémon in any way you like.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
    ],
)
