from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='4403e893-9522-58ff-861b-7ce12ad80af5',
    key='SM12',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.FlygonGX.Name',
    display_name='Flygon-GX',
    searchable_by=['Flygon-GX', 'Stage 2', 'GX', 'FlygonGX'],
    subtypes=['Stage 2', 'GX'],
    collector_number=110,
    set_code='SM12',
    regulation_mark=None,
    rarity=Rarities.RareHoloGX,
    hp=240,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Vibrava.Name',
    family_id=328,
    abilities=[
        Ability(
            title='Dusty Defense',
            game_text="As long as this Pokémon is your Active Pokémon, all of your Pokémon take 30 less damage from your opponent's attacks (after applying Weakness and Resistance).",
            passive=standard_passive("As long as this Pokémon is your Active Pokémon, all of your Pokémon take 30 less damage from your opponent's attacks (after applying Weakness and Resistance)."),
        ),
        Attack(
            title='Desert Hurricane',
            game_text='If there is any Stadium card in play, this attack does 120 more damage. Then, discard that Stadium card.',
            cost={PokemonTypes.FIGHTING: 3},
            damage=120,
            damage_operator='+',
            effect=standard_attack,
        ),
        Attack(
            title='Sonic Edge-GX',
            game_text="This attack's damage isn't affected by any effects on your opponent's Active Pokémon. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.FIGHTING: 3},
            damage=220,
            effect=standard_attack,
            gx=True,
        ),
    ],
)
