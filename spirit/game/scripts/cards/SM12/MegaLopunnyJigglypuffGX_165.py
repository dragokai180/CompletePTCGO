from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='f7a44dbb-826f-521a-a624-617aac446ba9',
    key='SM12',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.MegaLopunnyJigglypuffGX.Name',
    display_name='Mega Lopunny & Jigglypuff-GX',
    searchable_by=['Mega Lopunny & Jigglypuff-GX', 'Basic', 'TAG TEAM', 'GX', 'MegaLopunnyJigglypuffGX'],
    subtypes=['Basic', 'TAG TEAM', 'GX'],
    collector_number=165,
    set_code='SM12',
    regulation_mark=None,
    rarity=Rarities.RareHoloGX,
    hp=240,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=39,
    abilities=[
        Attack(
            title='Jumping Balloon',
            game_text="This attack does 60 more damage for each of your opponent's Pokémon-GX and Pokémon-EX in play.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
            damage_operator='+',
            effect=standard_attack,
        ),
        Attack(
            title='Puffy Smashers-GX',
            game_text="Your opponent's Active Pokémon is now Asleep. If this Pokémon has at least 4 extra Energy attached to it (in addition to this attack's cost), this attack does 200 damage to 1 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.) (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
            gx=True,
        ),
    ],
)
