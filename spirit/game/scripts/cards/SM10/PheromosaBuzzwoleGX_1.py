from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='1d79d88a-2212-5968-9602-04db2f4e7ee0',
    key='SM10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.PheromosaBuzzwoleGX.Name',
    display_name='Pheromosa & Buzzwole-GX',
    searchable_by=['Pheromosa & Buzzwole-GX', 'Basic', 'TAG TEAM', 'GX', 'Ultra Beast', 'PheromosaBuzzwoleGX'],
    subtypes=['Basic', 'TAG TEAM', 'GX', 'Ultra Beast'],
    collector_number=1,
    set_code='SM10',
    regulation_mark=None,
    rarity=Rarities.RareHoloGX,
    hp=260,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=794,
    abilities=[
        Attack(
            title='Jet Punch',
            game_text="This attack does 30 damage to 1 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.GRASS: 1},
            damage=30,
            effect=standard_attack,
        ),
        Attack(
            title='Elegant Sole',
            game_text="During your next turn, this Pokémon's Elegant Sole attack's base damage is 60.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=190,
            effect=standard_attack,
        ),
        Attack(
            title='Beast Game-GX',
            game_text="If your opponent's Pokémon is Knocked Out by damage from this attack, take 1 more Prize card. If this Pokémon has at least 7 extra Energy attached to it (in addition to this attack's cost), take 3 more Prize cards instead. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.GRASS: 1},
            damage=50,
            effect=standard_attack,
            gx=True,
        ),
    ],
)
