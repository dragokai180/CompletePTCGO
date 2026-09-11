from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw10 import blazing_claws, dark_clamp, leech_life, solar_transporter

card = PokemonCardDef(
    guid="680227dc-1f5d-5508-a796-d207a9b58bc2",
    key="BW1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Galvantula.Name",
    display_name="Galvantula",
    searchable_by=["Galvantula","Stage 1","Galvantula"],
    subtypes=["Stage 1"],
    collector_number=46,
    set_code="BW1",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Joltik.Name",
    abilities=[
        Attack(
            title="Electroweb",
            game_text="The Defending Pokémon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=20,
            effect=dark_clamp,
        ),
        Attack(
            title="Leech Life",
            game_text="Heal from this Pokémon the same amount of damage you did to the Defending Pokémon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=leech_life,
        ),
    ],
)
