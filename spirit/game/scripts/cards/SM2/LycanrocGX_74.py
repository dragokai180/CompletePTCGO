from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='da0e4d5c-0510-5949-9872-00916d52ec39',
    key='SM2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.LycanrocGX.Name',
    display_name='Lycanroc-GX',
    searchable_by=['Lycanroc-GX', 'Stage 1', 'GX', 'LycanrocGX'],
    subtypes=['Stage 1', 'GX'],
    collector_number=74,
    set_code='SM2',
    regulation_mark=None,
    rarity=Rarities.RareHoloGX,
    hp=200,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Rockruff.Name',
    family_id=744,
    abilities=[
        Ability(
            title='Bloodthirsty Eyes',
            game_text="When you play this Pokémon from your hand to evolve 1 of your Pokémon during your turn, you may switch 1 of your opponent's Benched Pokémon with their Active Pokémon.",
            effect=standard_ability,
            trigger=Triggers.ON_EVOLVE,
        ),
        Attack(
            title='Claw Slash',
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=110,
        ),
        Attack(
            title='Dangerous Rogue-GX',
            game_text="This attack does 50 damage for each of your opponent's Benched Pokémon. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            damage_operator='x',
            effect=standard_attack,
            gx=True,
        ),
    ],
)
