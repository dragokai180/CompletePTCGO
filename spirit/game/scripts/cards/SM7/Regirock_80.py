from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='199cb7bf-2eb7-52b4-9e4b-9fa82e2f3d73',
    key='SM7',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Regirock.Name',
    display_name='Regirock',
    searchable_by=['Regirock', 'Basic', 'Regirock'],
    subtypes=['Basic'],
    collector_number=80,
    set_code='SM7',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=377,
    abilities=[
        Attack(
            title='Enhanced Stomp',
            game_text='If this Pokémon has a Pokémon Tool card attached to it, this attack does 20 more damage.',
            cost={PokemonTypes.FIGHTING: 1},
            damage=20,
            damage_operator='+',
            effect=standard_attack,
        ),
        Attack(
            title='Hammer Arm',
            game_text="Discard the top card of your opponent's deck.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            effect=standard_attack,
        ),
    ],
)
