from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='557c7885-ead5-52ea-a8b7-c0460d1cee9a',
    key='XY5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.PrimalKyogreEX.Name',
    display_name='Primal Kyogre-EX',
    searchable_by=['Primal Kyogre-EX', 'MEGA', 'EX', 'PrimalKyogreEX'],
    subtypes=['MEGA', 'EX'],
    collector_number=55,
    set_code='XY5',
    regulation_mark=None,
    rarity=Rarities.RareHoloEX,
    hp=240,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.KyogreEX.Name',
    family_id=382,
    abilities=[
        Attack(
            title='Tidal Storm',
            game_text="Move 2 Energy from this Pokémon to 1 of your Benched Pokémon. This attack does 30 damage to each of your opponent's Benched Pokémon-EX. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.WATER: 3, PokemonTypes.COLORLESS: 1},
            damage=150,
            effect=standard_attack,
        ),
    ],
    passive=standard_passive('When you attach an Energy card from your hand to this Pokémon (except with an attack, Ability, or Trainer card), you may attach 2 Energy cards.'),
)
