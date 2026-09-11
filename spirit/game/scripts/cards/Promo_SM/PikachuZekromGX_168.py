from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='28727ad5-2472-5af3-8fc1-2ac363497d0f',
    key='Promo_SM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.PikachuZekromGX.Name',
    display_name='Pikachu & Zekrom-GX',
    searchable_by=['Pikachu & Zekrom-GX', 'Basic', 'TAG TEAM', 'GX', 'PikachuZekromGX'],
    subtypes=['Basic', 'TAG TEAM', 'GX'],
    collector_number=168,
    set_code='Promo_SM',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=240,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=25,
    abilities=[
        Attack(
            title='Full Blitz',
            game_text='Search your deck for up to 3 Lightning Energy cards and attach them to 1 of your Pokémon. Then, shuffle your deck.',
            cost={PokemonTypes.LIGHTNING: 3},
            damage=150,
            effect=standard_attack,
        ),
        Attack(
            title='Tag Bolt-GX',
            game_text="If this Pokémon has at least 3 extra Lightning Energy attached to it (in addition to this attack's cost), this attack does 170 damage to 1 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.) (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.LIGHTNING: 3},
            damage=200,
            effect=standard_attack,
            gx=True,
        ),
    ],
)
