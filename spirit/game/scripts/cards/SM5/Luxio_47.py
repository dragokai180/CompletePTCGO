from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='387ddc17-18c8-52f9-95fd-961113650380',
    key='SM5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Luxio.Name',
    display_name='Luxio',
    searchable_by=['Luxio', 'Stage 1', 'Luxio'],
    subtypes=['Stage 1'],
    collector_number=47,
    set_code='SM5',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Shinx.Name',
    family_id=403,
    abilities=[
        Attack(
            title='Disconnect',
            game_text="Your opponent can't play any Item cards from their hand during their next turn.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=standard_attack,
        ),
    ],
)
