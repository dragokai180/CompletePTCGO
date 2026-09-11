from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='47bbaaa2-458d-5d97-8b6b-1b95095fa168',
    key='XY7',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.PorygonZ.Name',
    display_name='Porygon-Z',
    searchable_by=['Porygon-Z', 'Stage 2', 'PorygonZ'],
    subtypes=['Stage 2'],
    collector_number=66,
    set_code='XY7',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Porygon2.Name',
    family_id=137,
    abilities=[
        Attack(
            title='Cyber Crush',
            game_text="Discard all Special Energy attached to each of your opponent's Pokémon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Slowing Beam',
            game_text="During your opponent's next turn, the Defending Pokémon's attacks cost Colorless more.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=70,
            effect=standard_attack,
        ),
    ],
)
