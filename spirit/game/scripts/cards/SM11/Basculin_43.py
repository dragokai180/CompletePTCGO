from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='fa7503ef-25c6-571c-9035-21ecb69cf5a2',
    key='SM11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Basculin.Name',
    display_name='Basculin',
    searchable_by=['Basculin', 'Basic', 'Basculin'],
    subtypes=['Basic'],
    collector_number=43,
    set_code='SM11',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=550,
    abilities=[
        Attack(
            title='Swarming Bites',
            game_text="This attack does 20 damage for each Basculin you have in play to 1 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Tackle',
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)
