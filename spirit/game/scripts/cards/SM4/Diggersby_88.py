from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='bfa76be0-70f2-5782-b02a-4eb8e24712dc',
    key='SM4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Diggersby.Name',
    display_name='Diggersby',
    searchable_by=['Diggersby', 'Stage 1', 'Diggersby'],
    subtypes=['Stage 1'],
    collector_number=88,
    set_code='SM4',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Bunnelby.Name',
    family_id=659,
    abilities=[
        Attack(
            title='Dig',
            game_text="Flip a coin. If heads, prevent all effects of attacks, including damage, done to this Pokémon during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
            effect=standard_attack,
        ),
        Attack(
            title='Hammer Arm',
            game_text="Discard the top card of your opponent's deck.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=90,
            effect=standard_attack,
        ),
    ],
)
