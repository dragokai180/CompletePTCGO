from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='df1634d2-fbce-5bbc-ad95-5e032c42bd32',
    key='SM11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.AerodactylGX.Name',
    display_name='Aerodactyl-GX',
    searchable_by=['Aerodactyl-GX', 'Stage 1', 'GX', 'AerodactylGX'],
    subtypes=['Stage 1', 'GX'],
    collector_number=106,
    set_code='SM11',
    regulation_mark=None,
    rarity=Rarities.RareHoloGX,
    hp=210,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.UnidentifiedFossil.Name',
    family_id=142,
    abilities=[
        Ability(
            title='Primal Winds',
            game_text="As long as this Pokémon is your Active Pokémon, your opponent's Basic Pokémon's attacks cost Colorless more.",
            passive=standard_passive("As long as this Pokémon is your Active Pokémon, your opponent's Basic Pokémon's attacks cost Colorless more."),
        ),
        Attack(
            title='Boulder Crush',
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=120,
        ),
        Attack(
            title='Wild Dive-GX',
            game_text="This attack does 50 damage times the amount of Energy attached to your opponent's Active Pokémon. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.FIGHTING: 1},
            damage=50,
            damage_operator='x',
            effect=standard_attack,
            gx=True,
        ),
    ],
)
