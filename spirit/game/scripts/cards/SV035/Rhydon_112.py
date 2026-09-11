from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='0f69a871-7b33-5f15-8ea2-5b5bc788e2c2',
    key='SV035',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Rhydon.Name',
    display_name='Rhydon',
    searchable_by=['Rhydon', 'Stage 1', 'Rhydon'],
    subtypes=['Stage 1'],
    collector_number=112,
    set_code='SV035',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Rhyhorn.Name',
    family_id=111,
    abilities=[
        Attack(
            title='Wrack Down',
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
        Attack(
            title='Charismatic Drill',
            game_text="If you played Giovanni's Charisma from your hand during this turn, this attack does 140 more damage.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=40,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
