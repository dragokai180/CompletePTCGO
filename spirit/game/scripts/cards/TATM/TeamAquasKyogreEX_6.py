from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='723cda7f-48c1-5abe-a843-987110011893',
    key='TATM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.TeamAquasKyogreEX.Name',
    display_name="Team Aqua's Kyogre-EX",
    searchable_by=["Team Aqua's Kyogre-EX", 'Basic', 'EX', 'TeamAquasKyogreEX'],
    subtypes=['Basic', 'EX'],
    collector_number=6,
    set_code='TATM',
    regulation_mark=None,
    rarity=Rarities.RareUltra,
    hp=190,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=382,
    abilities=[
        Ability(
            title='Power Saver',
            game_text="If there are 4 or fewer Team Aqua Pokémon in play, this Pokémon can't attack.",
            passive=standard_passive("If there are 4 or fewer Team Aqua Pokémon in play, this Pokémon can't attack."),
        ),
        Attack(
            title='Aqua Impact',
            game_text="This attack does 20 more damage for each Colorless in your opponent's Active Pokémon's Retreat Cost.",
            cost={PokemonTypes.WATER: 3, PokemonTypes.COLORLESS: 1},
            damage=80,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
