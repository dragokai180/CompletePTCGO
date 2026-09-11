from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='fbb7f558-d5a2-5d52-9ac7-80bbcd0f00e9',
    key='SM8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.SceptileGX.Name',
    display_name='Sceptile-GX',
    searchable_by=['Sceptile-GX', 'Stage 2', 'GX', 'SceptileGX'],
    subtypes=['Stage 2', 'GX'],
    collector_number=22,
    set_code='SM8',
    regulation_mark=None,
    rarity=Rarities.RareHoloGX,
    hp=230,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Grovyle.Name',
    family_id=252,
    abilities=[
        Attack(
            title='Mach Cut',
            game_text="Discard a Special Energy from your opponent's Active Pokémon.",
            cost={PokemonTypes.GRASS: 1},
            damage=60,
            effect=standard_attack,
        ),
        Attack(
            title='Leaf Cyclone',
            game_text='Move a Grass Energy from this Pokémon to 1 of your Benched Pokémon.',
            cost={PokemonTypes.GRASS: 2},
            damage=130,
            effect=standard_attack,
        ),
        Attack(
            title='Jungle Heal-GX',
            game_text="Heal all damage from each of your Pokémon that has any Grass Energy attached to it. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.GRASS: 1},
            effect=standard_attack,
            gx=True,
        ),
    ],
)
