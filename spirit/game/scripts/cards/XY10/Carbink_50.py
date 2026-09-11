from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='bc7c455b-c3b1-5bba-b4ff-dadac545497e',
    key='XY10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Carbink.Name',
    display_name='Carbink',
    searchable_by=['Carbink', 'Basic', 'Carbink'],
    subtypes=['Basic'],
    collector_number=50,
    set_code='XY10',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=703,
    abilities=[
        Ability(
            title='Safeguard',
            game_text="Prevent all effects of attacks, including damage, done to this Pokémon by your opponent's Pokémon-EX.",
            passive=standard_passive("Prevent all effects of attacks, including damage, done to this Pokémon by your opponent's Pokémon-EX."),
        ),
        Attack(
            title='Power Gem',
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
        ),
    ],
)
