from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='0cda948e-b014-5a4a-8841-f2936f79433f',
    key='HGSS4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.DarkraiCresseliaLEGEND.Name',
    display_name='Darkrai & Cresselia LEGEND',
    searchable_by=['Darkrai & Cresselia LEGEND', 'LEGEND', 'DarkraiCresseliaLEGEND'],
    subtypes=['LEGEND'],
    collector_number=99,
    set_code='HGSS4',
    regulation_mark=None,
    rarity=Rarities.Legendary,
    hp=150,
    elements=[PokemonTypes.DARKNESS, PokemonTypes.PSYCHIC],
    stage=PokemonStage.LEGEND,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    weakness_types=[PokemonTypes.FIGHTING, PokemonTypes.PSYCHIC],
    family_id=488,
    abilities=[
        Attack(
            title='Lost Crisis',
            game_text="Choose 2 Energy attached to Darkrai & Cresselia LEGEND and put them in the Lost Zone. If any of your opponent's Pokémon would be Knocked Out by damage from this attack, put that Pokémon and all cards attached to it in the Lost Zone instead of discarding it.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 2},
            damage=100,
            effect=standard_attack,
        ),
        Attack(
            title="Moon's Invite",
            game_text="Move as many damage counters on your opponent's Pokémon as you like to any of your opponent's other Pokémon in any way you like.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=standard_attack,
        ),
    ],
)
