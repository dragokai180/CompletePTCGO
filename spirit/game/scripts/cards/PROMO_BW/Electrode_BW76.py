from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack, flip_damage, recoil_attack

card = PokemonCardDef(
    guid="b07cf64c-48d7-5a98-afd6-2ad27baf4ff7",
    key="PROMO_BW",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Electrode.Name",
    display_name="Electrode",
    searchable_by=["Electrode","Stage 1","Electrode","Team Plasma"],
    subtypes=["Stage 1","Team Plasma"],
    collector_number=76,
    set_code="PROMO_BW",
    rarity=Rarities.RarePromo,
    hp=100,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Voltorb.Name",
    abilities=[
        Attack(
            title="Electribeam",
            game_text="Flip a coin. If heads, the Defending Pokémon is Paralyzed.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=20,
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
        Attack(
            title="Self Destruct",
            game_text="This Pokémon does 100 damage to itself.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
            effect=recoil_attack(100),
        ),
    ],
)
