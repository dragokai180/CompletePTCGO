from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='883c281a-30e0-5e08-a569-714076df30cc',
    key='SM12',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Sylveon.Name',
    display_name='Sylveon',
    searchable_by=['Sylveon', 'Stage 1', 'Sylveon'],
    subtypes=['Stage 1'],
    collector_number=155,
    set_code='SM12',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name',
    family_id=133,
    abilities=[
        Attack(
            title='Moonblast',
            game_text="During your opponent's next turn, the Defending Pokémon's attacks do 30 less damage (before applying Weakness and Resistance).",
            cost={PokemonTypes.FAIRY: 1},
            damage=30,
            effect=standard_attack,
        ),
        Attack(
            title='Beloved Pulse',
            game_text='If you played a TAG TEAM Supporter card from your hand during this turn, this attack does 80 more damage.',
            cost={PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
