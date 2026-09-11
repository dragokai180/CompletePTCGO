from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='d4ec40ca-defe-55f1-a28c-549ad23b2288',
    key='XY1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Rhyhorn.Name',
    display_name='Rhyhorn',
    searchable_by=['Rhyhorn', 'Basic', 'Rhyhorn'],
    subtypes=['Basic'],
    collector_number=60,
    set_code='XY1',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=111,
    abilities=[
        Attack(
            title='Dig Out',
            game_text='Discard the top card of your deck. If that card is a Fighting Energy, attach it to this Pokémon.',
            cost={PokemonTypes.FIGHTING: 1},
            damage=10,
            effect=standard_attack,
        ),
        Attack(
            title='Horn Drill',
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
        ),
    ],
)
