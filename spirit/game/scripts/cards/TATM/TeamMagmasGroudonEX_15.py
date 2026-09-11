from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='660d49ae-3d1c-57a8-805f-86d8f891499e',
    key='TATM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.TeamMagmasGroudonEX.Name',
    display_name="Team Magma's Groudon-EX",
    searchable_by=["Team Magma's Groudon-EX", 'Basic', 'EX', 'TeamMagmasGroudonEX'],
    subtypes=['Basic', 'EX'],
    collector_number=15,
    set_code='TATM',
    regulation_mark=None,
    rarity=Rarities.RareUltra,
    hp=190,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=383,
    abilities=[
        Ability(
            title='Power Saver',
            game_text="If there are 4 or fewer Team Magma Pokémon in play, this Pokémon can't attack.",
            passive=standard_passive("If there are 4 or fewer Team Magma Pokémon in play, this Pokémon can't attack."),
        ),
        Attack(
            title='Magma Quake',
            game_text="If your opponent's Active Pokémon already has any damage counters on it, this attack does 80 more damage.",
            cost={PokemonTypes.FIGHTING: 3, PokemonTypes.COLORLESS: 1},
            damage=80,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
