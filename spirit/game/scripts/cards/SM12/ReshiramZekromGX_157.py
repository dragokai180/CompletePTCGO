from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='d8b99594-9db9-5eb9-b0c1-7507837e6a86',
    key='SM12',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.ReshiramZekromGX.Name',
    display_name='Reshiram & Zekrom-GX',
    searchable_by=['Reshiram & Zekrom-GX', 'Basic', 'TAG TEAM', 'GX', 'ReshiramZekromGX'],
    subtypes=['Basic', 'TAG TEAM', 'GX'],
    collector_number=157,
    set_code='SM12',
    regulation_mark=None,
    rarity=Rarities.RareHoloGX,
    hp=270,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FAIRY,
    weakness_amount=2,
    family_id=643,
    abilities=[
        Attack(
            title='Fabled Flarebolts',
            game_text='Discard up to 3 in any combination of basic Fire and basic Lightning Energy cards from your Benched Pokémon. This attack does 90 damage for each card you discarded in this way.',
            cost={PokemonTypes.FIRE: 1, PokemonTypes.LIGHTNING: 1},
            damage=90,
            damage_operator='x',
            effect=standard_attack,
        ),
        Attack(
            title='Cross Break-GX',
            game_text="This attack does 170 damage to 1 of your opponent's Benched Pokémon. If you played N's Resolve from your hand during this turn, this attack also does 170 damage to 1 of your opponent's other Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.) (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.LIGHTNING: 2},
            effect=standard_attack,
            gx=True,
        ),
    ],
)
