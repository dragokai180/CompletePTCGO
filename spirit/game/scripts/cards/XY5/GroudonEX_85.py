from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='9f65cf35-8cfa-582f-b9f0-fabb13b2a38b',
    key='XY5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.GroudonEX.Name',
    display_name='Groudon-EX',
    searchable_by=['Groudon-EX', 'Basic', 'EX', 'GroudonEX'],
    subtypes=['Basic', 'EX'],
    collector_number=85,
    set_code='XY5',
    regulation_mark=None,
    rarity=Rarities.RareHoloEX,
    hp=180,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=383,
    abilities=[
        Attack(
            title='Rip Claw',
            game_text="Flip a coin. If heads, discard an Energy attached to your opponent's Active Pokémon.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=standard_attack,
        ),
        Attack(
            title='Massive Rend',
            cost={PokemonTypes.FIGHTING: 3, PokemonTypes.COLORLESS: 1},
            damage=130,
        ),
    ],
)
